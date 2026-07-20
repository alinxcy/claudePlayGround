# 棚卸し(Sync)手順

**手順の本体は `.claude/skills/memory-sync/SKILL.md` に移動しました。**

棚卸しを行うときは、そちらを参照してください。ユーザーが「棚卸しして」「claude.ai と
同期して」と言えば、`memory-sync` スキルが自動で発火します。

## なぜ移動したか

手順書が `memory/SYNC.md` と `SKILL.md` の両方にあると必ず片方が古くなるため、
SKILL.md を唯一の正とし、このファイルは誘導のみを残しています。

スキルは progressive disclosure（発火したときだけ本文が読まれる）が効くので、
手順を丸ごと SKILL.md に置いても普段のコンテキストを圧迫しません。

## このディレクトリの中身

| パス | 内容 |
|---|---|
| `README.md` | memory/ ディレクトリ全体の説明 |
| `snapshots/` | 記憶とスキル一覧のスナップショット（`YYYY-MM-DD.md`） |
| `CHANGELOG.md` | 棚卸し・還流の履歴（`memory-sync` と `skill-return` が共用） |
| `SYNC.md` | このファイル（誘導のみ） |
