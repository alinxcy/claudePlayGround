# SKILLS_ORIGIN.md の書式

派生リポジトリの `.claude/SKILLS_ORIGIN.md` に置く由来マニフェストの仕様。
`playground-spawn` が作成し、`skill-return` が読む。この2つのスキルを繋ぐ唯一の接点。

## 設計の意図

このファイルが答えるべき問いは3つ。

1. このスキルはどこから来たか（playground のどのコミット時点か）
2. このリポジトリで改変したか（YES なら還流候補）
3. 改変した場合、何を変えたか（還流時の説明になる）

3 を都度書くのが面倒なら空欄でもよい。1 と 2 が残っていれば `skill-return` が
`diff` で差分そのものは復元できる。ただし「なぜ変えたか」は diff からは分からないので、
可能なら1行残すと後で助かる。

## テンプレート

```markdown
# SKILLS_ORIGIN

このリポジトリの `.claude/skills/` と `.claude/agents/` は
[claudePlayGround](https://github.com/alinxcy/claudePlayGround) から持ち出したもの。

- 持ち出し元コミット: `<short-hash>`
- 持ち出し日: `YYYY-MM-DD`

## 持ち出したもの

| 名前 | 種別 | 元パス | 改変 | 備考 |
|---|---|---|---|---|
| skill-creator | skill | `.claude/skills/skill-creator` | なし | |
| md | skill | `.claude/skills/md` | なし | |
| prompt-writer | agent | `.claude/agents/prompt-writer.md` | なし | |

## このリポジトリで新規作成したもの

| 名前 | 種別 | 汎用性 | 備考 |
|---|---|---|---|
| （なし） | | | |

## 還流について

スキルを改変・新規作成したら、上の表の「改変」列を `あり` に更新し、
何を変えたかを備考に1行書く。playground に戻したくなったら `skill-return` を使う。
```

## 運用ルール

**改変列の更新タイミング** — スキルを編集したコミットと同じコミットで更新するのが理想だが、
忘れても `skill-return` が diff で検出するので致命的ではない。気づいたときに直す。

**新規作成の「汎用性」列** — このリポジトリ固有か、他でも使えるかの判断。
`高`（他プロジェクトでも使える）、`中`（似た種類のプロジェクトなら）、
`低`（このリポジトリ専用）の3段階。`高` と `中` が還流候補になる。

**持ち出し元コミットの更新** — playground 側が更新されても、このファイルの hash は
持ち出し時点のまま据え置く。これは「いつの版をベースにしたか」の記録であって、
追従の記録ではない。playground の新しい版を取り込みたくなったら、
その時点で hash を更新して差分を確認する。

## 最小構成

面倒なら以下まで削ってよい。これだけあれば `skill-return` は動く。

```markdown
# SKILLS_ORIGIN
playground@abc1234 (2026-07-19) から: skill-creator, md, prompt-writer
```
