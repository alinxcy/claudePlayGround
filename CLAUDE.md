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

2. **「これを使って何か作って」と言われたら、`playground-spawn` スキルを使って
   新しい別リポジトリで作業する。** このリポジトリの中身は参照専用として読み込み、
   成果物は新リポジトリに置きます。

3. **`git push` / `git commit` をこのリポジトリに対して行う前に、必ず確認を取る。**
   下の「更新してよい例外ケース」に該当することを確認できたときだけ実行します。

4. 迷ったら「playground は触らない」を選ぶ。読むだけなら常に自由です。

## 更新してよい例外ケース

以下のいずれかに当てはまるときに限り、このリポジトリを更新してよい。
いずれも対応するスキルが用意されているので、それに従うこと。

| ケース | トリガー | 使うスキル |
|---|---|---|
| 棚卸し | 「棚卸しして」「claude.ai と同期して」 | `memory-sync` |
| 還流 | 「playground に戻して」「還流して」 | `skill-return` |
| 新機能の反映 | ユーザーが新機能に気づいたとき | `memory-sync` (Step 6) |
| 運用ルール改訂 | このファイルを変えるとユーザーが決めたとき | （手動） |

上記以外で書き込みが必要に見えた場合は、実行せずユーザーに確認する。

## 3つの運用スキル

このリポジトリの運用は以下の3スキルで回します。いずれも playground 専用であり、
派生リポジトリには持ち出しません。

```
        claude.ai
            │
            │ memory-sync（棚卸し）
            ▼
      claudePlayGround
            │  ▲
 playground-spawn │ skill-return
      （切り出し） │ （還流）
            ▼  │
      派生リポジトリ（実際の開発）
```

- **`playground-spawn`** — 必要なスキルを選んで新リポジトリを立てる。
  由来を `.claude/SKILLS_ORIGIN.md` に記録するのが要点。
- **`skill-return`** — 派生リポジトリで育ったスキルを playground に戻す。
  マニフェストを手がかりに差分を検出する。
- **`memory-sync`** — claude.ai 側との差分を取り込む。半自動。

## ディレクトリ構成

| パス | 役割 | 自動ロード |
|---|---|---|
| `.claude/skills/` | 有効化済みの Skill 群（claude.ai の Skills に対応） | される |
| `.claude/agents/` | サブエージェント定義 | される |
| `skill-library/` | Anthropic 公式 example スキルの参照用ストック | されない |
| `builtins-reconstructed/` | Claude Code CLI 組み込み機能の再構築版（ベストエフォート） | されない |
| `memory/` | claude.ai 側 Memory のスナップショットと棚卸し履歴 | されない |

`skill-library/` と `builtins-reconstructed/` は `.claude/skills/` の外にあるため
自動ロードされません。使いたいときは新リポジトリの `.claude/skills/` に**コピー**します
（移動ではなくコピー。playground 側は残す）。

## 新しいプロジェクトを始めるとき

`playground-spawn` スキルに詳細な手順がありますが、要点だけ再掲します。

1. 今回のタスクに必要なスキルを3〜5個に絞って選ぶ
2. `gh repo create` で新リポジトリを作る
3. 選んだスキルを新リポジトリの `.claude/skills/` に**コピー**する
4. `.claude/SKILLS_ORIGIN.md` に由来（playground のコミットハッシュ）を記録する
5. 新リポジトリ固有の `CLAUDE.md` を**新規に書く**
   — このファイルをコピーしないこと。新リポジトリは playground ではないため、
   ここに書かれた「編集しない」ルールを持ち込むと開発できなくなります。
6. 以降 `claudePlayGround` には書き込まない

## 参考

- Skill の作成・診断・発掘: `.claude/skills/skill-creator`,
  `.claude/skills/skill-optimizer`, `.claude/skills/skill-harvester`
- 仕様の壁打ち: `.claude/skills/spec-sparring`
- Claude Code 設定リファレンス: <https://code.claude.com/docs/en/settings>
