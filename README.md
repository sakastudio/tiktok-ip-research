# AI動画IP創出研究 — 調査レポート図解まとめ

縦型ショート動画で新規IPをゼロから育てるための調査・検証レポート3本を、レビュー用の単一HTML図解ページに起こしたもの。

## 構成

| パス | 内容 |
|---|---|
| `index.html` | ポータル（図解一覧・読む順番・コメントの使い方） |
| `ai-vs-3d/index.html` | 図解: AIを完パケにするか、3Dを完パケにするか |
| `worldview-format/index.html` | 図解: 世界観適性とフォーマットの集中調査 |
| `deep-verification/index.html` | 図解: 徹底検証レビュー: 観察メモ + AI vs 3Dレポート |
| `<slug>/source/index.html` | 原文（元Markdownをそのまま整形表示） |
| `sources/*.md` | 元Markdown原本 |
| `tools/build-sources.py` | `sources/*.md` → 原文ページの生成スクリプト |

図解は元Markdownを唯一の正として起こしており、事実の追加・改変はしていない。原文ページは pandoc（gfm → html5）でそのまま変換したもので、内容の編集は一切していない。

各ページからの導線は次のとおり。

- ポータル → 図解（カード全体クリック）／原文（カード右下の「原文」）
- 図解 → まとめトップ／原文（hero直下）
- 原文 → 図解に戻る／まとめトップ／Markdown原本（上部バー）

## 原文ページの再生成

```
python3 tools/build-sources.py
```

pandoc が必要（`brew install pandoc`）。`sources/*.md` を更新してから実行すると `<slug>/source/index.html` が上書きされる。対象ドキュメントの追加はスクリプト冒頭の `DOCS` に1エントリ足す。

## 図解を追加するとき

トップページ（`index.html`）は一覧性を保つためのポータルで、各図解ページとは意図的に別デザインにしてある（ダークヒーロー＋カードグリッド）。追加時は次の2つを更新する。

1. `<新スラッグ>/index.html` を追加する。ベースは `.claude/skills/create-infographic-light/assets/template.html`。CSSとコメント機能JSはverbatim維持し、`STORAGE_KEY` と `COPY_TITLE` はページ固有値にする（他ページと同じだとlocalStorage上でコメントが混ざる）。hero直下に `<p><a href="../">まとめトップに戻る</a>　/　<a href="source/">原文（Markdown）を見る</a></p>` を置く。
2. 元Markdownを `sources/` に置き、`tools/build-sources.py` の `DOCS` にエントリを足して実行する（原文ページが生成される）。
3. `index.html` の `.card-grid` にカードを1枚追加し、`.stat-row` の3つの数値（図解ページ数・元ドキュメント行数・コメント可能ブロック数）と `.sec-count` の件数を更新する。

カード内のタイトルは `<a>` で包む（`::after` でカード全体をクリック領域に広げる実装）。カードそのものを `<a>` にすると「原文」リンクが入れ子アンカーになって壊れるので注意。

カードは `style="--accent:#XXXXXX; --accent-bg:#YYYYYY;"` でアクセント色を指定する。既出の色は 1=インディゴ `#4F46E5` / 2=ティール `#0D9488` / 3=アンバー `#D97706`。`.card-kind`（方針判断・企画設計・敵対的検証など）はレポートの性格を一語で表すラベル。

## レビューコメント機能

各図解ページには、レビュー用のコメント機能を組み込んである。

- 本文のテキストを選択すると「コメントを追加」ボタンが出る
- 図や表はブロック右上の「コメント」ボタンから付ける（タッチ端末では常時表示）
- コメントは左下のパネルに集まる。クリックで該当箇所へジャンプ、編集・削除も可能
- 「すべてコピー」でMarkdownとして書き出せる

コメントはブラウザのlocalStorageに保存されるため、同じ端末・同じブラウザでのみ復元される。ページごとに別のキーで保存されるので混ざらない。

## 技術メモ

- 各ページは単一の `index.html`（インラインCSS + vanilla JS）。ビルド不要、`file://` で直接開いても動く
- 外部依存なし（CDN参照なし）
- GitHub Pages で公開。Jekyll処理を無効化するため `.nojekyll` を置いている
