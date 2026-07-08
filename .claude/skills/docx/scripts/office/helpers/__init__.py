import os
import stat
import tempfile
import zipfile
from pathlib import Path

OOXML_FAMILY = {
    ".docx": "docx",
    ".dotx": "docx",
    ".pptx": "pptx",
    ".potx": "pptx",
    ".xlsx": "xlsx",
    ".xltx": "xlsx",
}


def safe_extract(zf: zipfile.ZipFile, dest: Path) -> None:
    dest = dest.resolve()
    for m in zf.infolist():
        if stat.S_ISLNK(m.external_attr >> 16):
            raise ValueError(f"symlink archive entry not allowed: {m.filename!r}")
        target = (dest / m.filename).resolve()
        if not target.is_relative_to(dest):
            raise ValueError(f"unsafe archive entry: {m.filename!r}")
        zf.extract(m, dest)


def rezip(src_dir: Path, out_path: Path) -> None:
    files = sorted(p for p in src_dir.rglob("*") if p.is_file())
    ct = src_dir / "[Content_Types].xml"
    fd, tmp_name = tempfile.mkstemp(
        prefix=out_path.name + ".", suffix=".tmp", dir=out_path.parent
    )
    tmp_out = Path(tmp_name)
    try:
        with os.fdopen(fd, "wb") as fh:
            with zipfile.ZipFile(fh, "w", zipfile.ZIP_DEFLATED) as zf:
                if ct.exists():
                    zf.write(ct, ct.relative_to(src_dir), compress_type=zipfile.ZIP_STORED)
                for f in files:
                    if f == ct:
                        continue
                    zf.write(f, f.relative_to(src_dir))
        os.replace(tmp_out, out_path)
    finally:
        if tmp_out.exists():
            tmp_out.unlink()
