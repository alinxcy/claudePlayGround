---
name: memory-sync
description: claude.ai 側で増えた Skill / Agent / Memory と claudePlayGround の差分を突き合わせて取り込む棚卸し手順。ユーザーが「棚卸しして」「claude.ai と同期して」「スキルの差分を見て」と言ったときに使用する。git のブランチ同期やファイル・フォルダの一般的な同期作業とは無関係なので、それらには使わない。playground への書き込みを伴うため、削除を含む操作は必ず承認を得る。
---

# Memory Sync

claude.ai 側は使うほどに Skill も Memory も増えていく。playground はそれを追いかけないと
古くなる。このスキルはその差分を定期的に取り込むためのもの。

claude.ai の Memory と Skill 一覧は API から機械的に取れないため、**半自動**の手順になる。
ユーザーに claude.ai 側で情報を書き出してもらい、それを受け取って差分を取る。
この人手が挟まる点が本質的な制約なので、手順は「聞き方」まで含めて定めてある。

## 2つのモード

着手前にどちらを行うか確認する。

**ライト棚卸し** — Skill / Agent の差分確認のみ。数分。
**フル棚卸し** — 上記に加えて Memory のスナップショット取得と差分分析。

「棚卸しして」とだけ言われたらライトを既定とし、フルにするか尋ねる。

## Step 1: claude.ai 側からの情報取得

ユーザーに claude.ai のチャットで以下を実行してもらい、出力を貼ってもらう。
プロンプトはそのまま提示してよい。

**Skill / Agent 一覧（両モード共通）**

> 今あなたが使えるスキルの一覧を、名前と description の1行要約でリストアップして。
> ユーザースキル・公式スキル・example スキルを区別して。

**Memory（フル棚卸しのみ）**

> これまでの会話から覚えていることを、カテゴリ別に箇条書きで整理して出力して。

貼られるまで先に進まない。ここが揃わないと差分が取れない。

## Step 2: Skill の差分

`.claude/skills/` のフォルダ名一覧と、貼られた claude.ai 側の一覧を突き合わせる。
`skill-library/` と `builtins-reconstructed/` も参照する（そこに既にあるものを
「playground に無い」と誤判定しないため）。

差分を3分類で報告する。

| 分類 | 意味 | 既定の扱い |
|---|---|---|
| 追加候補 | claude.ai にあって playground に無い | 承認後に追加 |
| 削除候補 | playground にあって claude.ai で使われていない | **必ず承認後**。迷ったら残す |
| 更新候補 | 両方にあるが内容が変わっていそう | 差分を見せて判断を仰ぐ |

削除は情報が失われる操作。「claude.ai で見当たらない」は「不要」を意味しない
（ユーザーが一覧に書き漏らした可能性もある）。判断に迷ったら残す。

## Step 3: Skill の取り込み

追加・更新が承認されたものについて、SKILL.md の内容をユーザーに書き出してもらい、
`.claude/skills/<name>/SKILL.md` として配置する。

配置前に `skill-optimizer` を通して、既存スキルと description の発火条件が
衝突していないか確認する。スキルが増えるほど誤発火のリスクが上がるので、
数が増えてきたらここは省略しない。

## Step 4: Agent の差分

`.claude/agents/` に対して Step 2〜3 と同じことを行う。

## Step 5: Memory のスナップショット（フル棚卸しのみ）

1. 貼られた記憶の要約を `memory/snapshots/YYYY-MM-DD.md` として保存する。
   書式は `memory/snapshots/README.md` を参照。
2. 直前のスナップショットと比較し、以下を探す。
   - 新しく登場した作業パターン・繰り返し
   - 前回から消えたトピック（関心が移った可能性）
   - 前提条件の変化（使用ツール、環境、役割）
3. 繰り返し登場するパターンが見つかったら `skill-harvester` に渡す。

   > `memory/snapshots/` の直近2ファイルの差分から、Skill 化できそうな
   > 手順・パターンを探して提案して。

**個人情報の扱い** — Memory には機微な内容が含まれうる。playground が Public の場合、
保存前に内容を確認し、必要なら抽象度を上げるか該当ファイルを `.gitignore` に追加する。
ユーザーに判断を仰ぐこと。勝手に載せない。

## Step 6: builtins-reconstructed / skill-library の更新

claude.ai や Claude Code に新機能が増えていた場合、該当するベストエフォート版
ドキュメントを追記・更新する。既存 README の表形式に合わせる。

新機能の有無は以下で確認できる。

- Claude Code ドキュメント索引: <https://code.claude.com/docs/en/claude_code_docs_map.md>
- 同索引内の "What's New" セクション

## Step 7: 記録とコミット

`memory/CHANGELOG.md` に1行追記する。

```
- YYYY-MM-DD: <ライト|フル> 棚卸し。skill +N/-M、agent +N、memory の主な変化を1文で。
```

コミットして push する。

```bash
git add -A
git commit -m "sync: YYYY-MM-DD <ライト|フル>棚卸し (skill +N)"
git push
```

棚卸しは CLAUDE.md の「更新してよい例外ケース」に該当するため実行してよい。
ただし削除を含む場合のみ、push 前にもう一度確認する。

## 頻度の目安

決まった周期は設けない。以下が自然なタイミング。

- claude.ai 側で新しいスキルを3つ以上作ったとき
- 派生リポジトリでの作業中に「playground のスキルが古い」と感じたとき
- Claude Code / claude.ai に大きなアップデートがあったとき
- `skill-return` で還流したついで（同じ CHANGELOG を使うので相性がよい）

`/loop` で定期実行も可能だが、Step 1 に人手が要るため実用上は手動起動が現実的。

## このスキルがやらないこと

- 新リポジトリの作成（`playground-spawn`）
- 派生リポジトリからの還流（`skill-return`）
- Skill 候補の発掘そのもの（`skill-harvester` に委譲）
- スキルの品質診断（`skill-optimizer` に委譲）
