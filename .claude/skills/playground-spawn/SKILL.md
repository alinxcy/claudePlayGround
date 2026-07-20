---
name: playground-spawn
description: claudePlayGround（ベースリポジトリ）から新しいプロジェクトリポジトリを切り出す手順。必要なSkill/Agentを選定してコピーし、由来マニフェストを残し、新規CLAUDE.mdを書くところまでを行う。ユーザーが playground で「〜を作りたい」「新しいプロジェクトを始めたい」「別リポジトリを切って」と言ったとき、また playground 内で実装作業が始まりそうになったときは必ず使用する。playground 自体を編集しそうになったら、その前にこのスキルを検討すること。
---

# Playground Spawn

playground は素材置き場であり、開発の現場ではない。開発が始まるときは、必要な素材だけを
持ち出して新しいリポジトリを立てる。このスキルはその「持ち出し」を手順化したもの。

一番大事なのは **由来を記録すること**。どのスキルをどの時点の playground から持ってきたかが
残っていないと、あとで playground に還流させるとき（`skill-return`）に何が変わったのか
分からなくなる。マニフェストはそのための唯一の手がかりなので、必ず書く。

## いつ使うか

- playground で「〜を作りたい」と相談が始まり、実装フェーズに入るとき
- playground のファイルを編集したくなったとき（それは大抵、新リポジトリを切るべきサイン）
- 既存の別リポジトリに、playground のスキルを後から持ち込みたいとき（Step 1〜4のみ実行）

## Workflow

### Step 1: タスクの把握とスキル選定

まず何を作るのかを確認する。曖昧なら仕様を詰める段階なので、`spec-sparring` を先に
使うことを提案してよい。

タスクが決まったら、`.claude/skills/` と `.claude/agents/` の各 description を読み、
今回必要になりそうなものを **3〜5個に絞って** 候補として提示する。全部持っていくと
新リポジトリが肥大して、Claude が毎回関係ないスキルの description を読むことになる。

`skill-library/` と `builtins-reconstructed/` も候補になりうるので、タスクに直結する
ものがあれば併せて提示する。これらは playground では自動ロードされていないが、
新リポジトリの `.claude/skills/` に置けば有効になる。

提示は以下の形式で行い、ユーザーに取捨選択してもらう。

```
## 持ち出し候補

### 必須
- skill-creator — 開発中に新しいスキルを作る可能性が高いため

### 推奨
- md — README や設計メモを書くため

### 任意（タスク次第）
- frontend-design — UI を作るなら

過不足があれば教えてください。
```

**持ち出してはいけないもの**

`playground-spawn`（このスキル自身）、`memory-sync`、`skill-return` は playground 専用。
新リポジトリにあっても意味がなく、むしろ誤発火の原因になるので候補に含めない。

### Step 2: 新リポジトリの作成

リポジトリ名をユーザーに確認する。決まっていなければタスク内容から2〜3案を提案する。

作成は `gh` CLI を使う。claude.ai 側の GitHub 連携は権限が制限されている場合があるため、
Claude Code から実行するのが確実。

```bash
gh repo create <name> --private --clone
cd <name>
```

Public にするか Private にするかは必ず確認する。playground 由来のスキルに業務固有の
情報が含まれている可能性があるため、迷ったら Private を選ぶ。

### Step 3: スキルのコピー

承認されたスキル/エージェントのフォルダを、**コピー**する（移動ではない。playground 側は
必ず残す）。

```bash
mkdir -p .claude/skills .claude/agents
cp -r <playground>/.claude/skills/<name> .claude/skills/
cp <playground>/.claude/agents/<name>.md .claude/agents/
```

`skill-library/` や `builtins-reconstructed/` から持ち出す場合も、コピー先は
`.claude/skills/<name>/` にする。そこに置かないと自動ロードされない。

### Step 4: 由来マニフェストの作成

`.claude/SKILLS_ORIGIN.md` を作成する。これが `skill-return` の入力になるので、
省略しない。書式は `references/manifest-format.md` を参照。

コピー元のコミットハッシュは playground 側で取得する。

```bash
git -C <playground> rev-parse --short HEAD
```

### Step 5: 新リポジトリの CLAUDE.md を書く

**playground の CLAUDE.md をコピーしてはいけない。** あれは「このリポジトリを編集するな」と
書いてあるファイルであり、新リポジトリに持ち込むと開発が一切できなくなる。

新規に、そのプロジェクト固有の内容で書く。最低限これらを含める。

- プロジェクトの目的（1〜2文）
- 技術スタック
- ビルド・テスト・実行のコマンド
- `.claude/SKILLS_ORIGIN.md` の存在と役割への言及。具体的には、コピー元スキルを
  このリポジトリで改良した場合、`skill-return` で playground に還流させる余地があると
  一文書いておく。これがないと還流の経路が忘れられる。

コードベースがまだ空なら `/init` は使えないので手で書く。ある程度実装が進んでから
`/init` で補強するとよい。

### Step 6: 初回コミット

```bash
git add -A
git commit -m "init: playground から <N> スキルを持ち出してセットアップ"
git push -u origin main
```

playground 側には一切書き込んでいないことを確認してから完了を報告する。

## 完了報告のフォーマット

```
新リポジトリ <name> を作成しました。

持ち出したスキル: <list>
由来マニフェスト: .claude/SKILLS_ORIGIN.md（playground@<hash> 基準）

playground は変更していません。
このリポジトリでスキルを改良したら、skill-return で playground に戻せます。
```

## よくある失敗

**playground の CLAUDE.md をコピーする** — 最も致命的。新リポジトリが凍結される。

**スキルを移動してしまう** — playground が欠ける。必ず `cp`、`mv` は使わない。

**マニフェストを省略する** — その場は動くが、還流経路が失われる。3行で済むので必ず書く。

**スキルを全部持っていく** — description が増えて誤発火が起きやすくなる。絞る。

## このスキルがやらないこと

- playground 自体の更新（原則しない。CLAUDE.md の例外ケースを参照）
- 新リポジトリでの実装作業そのもの（セットアップまでが担当）
- playground への還流（`skill-return` の担当）
