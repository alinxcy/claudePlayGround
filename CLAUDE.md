# CLAUDE.md — claudePlayGround

このリポジトリは、claude.ai 側で育った Skills / Agents / Memory を Claude Code でも
使えるようにするための **ベースリポジトリ(playground)** です。

## このリポジトリの位置づけ

ここは「素材置き場」であり、日々の開発プロジェクトそのものではありません。
実際の開発は、このリポジトリを土台にして**別リポジトリを新規作成**して行います。
そのため、このリポジトリ自体は原則として変更しません。

## デフォルトの振る舞い（最重要）

1. **このリポジトリのファイルは、明示的な指示がない限り編集・削除・追加しない。**
   対象: `.claude/skills/**`, `.claude/agents/**`, `builtins-reconstructed/**`,
   `skill-library/**`, `memory/**`, `README.md`, この `CLAUDE.md` 自身。

2. **「これを使って何か作って」と言われたら、新しい別リポジトリで作業する。**
   このリポジトリの中身は参照専用として読み込み、成果物は新リポジトリに置きます。

3. **`git push` / `git commit` をこのリポジトリに対して行う前に、必ず確認を取る。**
   下の「更新してよい例外ケース」に該当することを確認できたときだけ実行します。

4. 迷ったら「playground は触らない」を選ぶ。読むだけなら常に自由です。

## 更新してよい例外ケース

以下のいずれかに当てはまるときに限り、このリポジトリを更新してよい。

- **棚卸し(sync)**: ユーザーが「棚卸しして」「sync して」「memory-sync して」等と
  明示的に指示したとき。手順は `memory/SYNC.md` に従う。
- **良い Skill / Agent ができたとき**: 別リポジトリでの作業中に汎用性の高い
  Skill や Agent が生まれ、ユーザーが「これは playground に入れて」と承認したとき。
  `.claude/skills/<name>/` または `.claude/agents/` に追加する。
- **新機能の反映**: claude.ai / Claude Code に新しい機能や概念が増え、
  `builtins-reconstructed/` や `skill-library/` に反映すべきとユーザーが判断したとき。
- **このファイル自身の改訂**: 運用ルールを変えるとユーザーが決めたとき。

上記以外で書き込みが必要に見えた場合は、実行せずユーザーに確認する。

## ディレクトリ構成

| パス | 役割 | 自動ロード |
|---|---|---|
| `.claude/skills/` | 有効化済みの Skill 群（claude.ai の Skills に対応） | される |
| `.claude/agents/` | サブエージェント定義 | される |
| `skill-library/` | Anthropic 公式 example スキルの参照用ストック | されない |
| `builtins-reconstructed/` | Claude Code CLI 組み込み機能の再構築版（ベストエフォート） | されない |
| `memory/` | claude.ai 側 Memory のスナップショットと棚卸し手順 | されない |

`skill-library/` と `builtins-reconstructed/` は `.claude/skills/` の外にあるため
自動ロードされません。使いたいときは新リポジトリの `.claude/skills/` に**コピー**します
（移動ではなくコピー。playground 側は残す）。

## 新しいプロジェクトを始めるときの手順

1. このリポジトリを読み込み、今回のタスクに関係しそうな `.claude/skills/*` と
   `.claude/agents/*` を確認する。参照元として `skill-library/`,
   `builtins-reconstructed/` も見てよい。
2. 新しい GitHub リポジトリを作成する（またはユーザーに作成してもらう）。
3. 必要な Skill / Agent のフォルダ**だけ**を、新リポジトリの `.claude/skills/`,
   `.claude/agents/` にコピーする。
4. 新リポジトリ側に、そのプロジェクト固有の `CLAUDE.md` を新規に書く。
   このファイルをそのままコピーしないこと（新リポジトリは playground ではないため、
   ここに書かれた「編集しない」ルールは当てはまらない）。
5. 以降 `claudePlayGround` には書き込まない。

## 棚卸し(sync)について

claude.ai 側では Skill や Memory がユーザーの利用に応じて自然に増えていきます。
定期的に playground と突き合わせて差分を取り込むのが「棚卸し」です。

手順は `memory/SYNC.md` を参照してください。棚卸しの実行自体は、
ユーザーが明示的に依頼したときのみ行います。

## 参考

- Skill の書き方・診断・発掘: `.claude/skills/skill-creator`,
  `.claude/skills/skill-optimizer`, `.claude/skills/skill-harvester`
- Claude Code の設定リファレンス: <https://code.claude.com/docs/en/settings>
