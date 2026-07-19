# snapshots/

claude.ai 側の Memory と Skills 一覧のスナップショットを、`YYYY-MM-DD.md` の
ファイル名で保存する。

## 推奨フォーマット

```markdown
# Snapshot YYYY-MM-DD

## Skills（claude.ai 側）

### ユーザースキル
- skill-name — 1行要約

### 公式スキル
- skill-name — 1行要約

## Agents
- agent-name — 1行要約

## Memory 要約

### 環境・ツール
- ...

### 進行中のプロジェクト
- ...

### 作業パターン・好み
- ...
```

## 注意

機微な情報（個人情報、認証情報、業務上の秘密）は書き込まない。書く必要がある場合は
ファイルを `.gitignore` に追加するか、抽象度を上げて記載する。
