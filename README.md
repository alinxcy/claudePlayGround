# claudePlayGround

claude.ai で育てた Skills / Agents / Memory を Claude Code でも使うための
ベースリポジトリ。**このリポジトリ自体は基本的に更新しない**（詳細は `CLAUDE.md`）。

## 使い方

```bash
git clone https://github.com/alinxcy/claudePlayGround.git
cd claudePlayGround
claude
```

起動すると `CLAUDE.md` が自動で読み込まれ、Claude Code は「playground は参照専用、
実作業は別リポジトリで」というルールに従って動く。

## 構成

| パス | 役割 | 自動ロード |
|---|---|---|
| `.claude/skills/` | 有効化済み Skill 群 | される |
| `.claude/agents/` | サブエージェント定義 | される |
| `skill-library/` | 公式 example スキルの参照用ストック | されない |
| `builtins-reconstructed/` | Claude Code 組み込み機能の再構築版 | されない |
| `memory/` | Memory スナップショットと棚卸し手順 | されない |

## 典型的なフロー

1. このリポジトリで `claude` を起動して相談する
2. 何か作ることになったら、新しいリポジトリを切ってそちらで開発する
3. 必要なスキルだけ新リポジトリの `.claude/skills/` にコピーする
4. 良いスキルができたら playground に戻す（要承認）
5. ときどき棚卸しして claude.ai 側との差分を取り込む（`memory/SYNC.md`）
