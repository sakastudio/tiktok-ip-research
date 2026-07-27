#!/usr/bin/env python3
"""元Markdownを整形表示する原文ページを生成する。

  python3 tools/build-sources.py

sources/*.md を pandoc (gfm -> html5) で変換し、<slug>/source/index.html を書き出す。
図解ページとは意図的に別デザイン（プレーンなドキュメント表示）にしてある。
"""

import html
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "sources"

DOCS = [
    {
        "slug": "ai-vs-3d",
        "md": "report-2026-07-27-ai-vs-3d.md",
        "title": "AIを完パケにするか、3Dを完パケにするか",
        "accent": "#4F46E5",
    },
    {
        "slug": "worldview-format",
        "md": "report-2026-07-27-worldview-format.md",
        "title": "世界観適性とフォーマットの集中調査",
        "accent": "#0D9488",
    },
    {
        "slug": "deep-verification",
        "md": "review-2026-07-27-deep-verification.md",
        "title": "徹底検証レビュー: 観察メモ + AI vs 3Dレポート",
        "accent": "#D97706",
    },
]

PAGE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>原文: {title}</title>
<style>
  :root{{
    --accent:{accent};
    --border:#E2E8F0;
    --text:#0F172A;
    --text-muted:#475569;
    --text-subtle:#64748B;
  }}
  *{{box-sizing:border-box;}}
  html,body{{
    margin:0; width:100%;
    background:#FFFFFF; color:var(--text);
    overflow-x:hidden;
    font-family:-apple-system,BlinkMacSystemFont,"Hiragino Kaku Gothic ProN","Hiragino Sans",system-ui,sans-serif;
    line-height:1.9;
  }}
  p,li,td,th,blockquote{{ overflow-wrap:anywhere; }}
  a{{ color:var(--accent); }}

  .topbar{{
    position:sticky; top:0; z-index:50;
    display:flex; align-items:center; gap:14px; flex-wrap:wrap;
    background:rgba(255,255,255,.94);
    backdrop-filter:saturate(180%) blur(8px);
    border-bottom:1px solid var(--border);
    padding:11px 20px;
  }}
  .topbar .kind{{
    font-size:11px; font-weight:700; letter-spacing:.1em;
    color:#fff; background:var(--accent);
    border-radius:999px; padding:3px 11px;
  }}
  .topbar a{{ font-size:13px; font-weight:600; text-decoration:none; color:var(--text-muted); }}
  .topbar a:hover{{ color:var(--accent); text-decoration:underline; }}
  .topbar .sep{{ color:#CBD5E1; font-size:12px; }}
  .topbar .file{{
    margin-left:auto;
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
    font-size:11px; color:var(--text-subtle);
  }}

  .doc{{
    max-width:760px;
    margin:0 auto;
    padding:34px 20px 120px;
    font-size:15px;
  }}
  .doc h1{{
    font-size:25px; line-height:1.5;
    margin:0 0 26px;
    padding-bottom:14px;
    border-bottom:3px solid var(--accent);
  }}
  .doc h2{{
    font-size:19.5px; line-height:1.55;
    margin:52px 0 14px;
    padding-bottom:8px;
    border-bottom:1px solid var(--border);
  }}
  .doc h3{{ font-size:16.5px; margin:34px 0 10px; }}
  .doc h4{{ font-size:14.5px; margin:26px 0 8px; color:var(--text-muted); }}
  .doc p{{ margin:14px 0; }}
  .doc ul,.doc ol{{ padding-left:24px; margin:14px 0; }}
  .doc li{{ margin:7px 0; }}
  .doc blockquote{{
    margin:18px 0;
    border-left:4px solid var(--accent);
    background:#F8FAFC;
    border-radius:0 8px 8px 0;
    padding:2px 18px;
    color:var(--text-muted);
    font-size:14px;
  }}
  .doc hr{{ border:none; border-top:1px solid var(--border); margin:44px 0; }}
  .doc table{{
    border-collapse:collapse; width:100%;
    font-size:13px; line-height:1.7; min-width:520px;
  }}
  .doc .table-wrap{{
    overflow-x:auto;
    border:1px solid var(--border);
    border-radius:10px;
    margin:18px 0;
  }}
  .doc th,.doc td{{
    text-align:left; padding:9px 12px;
    border-bottom:1px solid var(--border);
    vertical-align:top;
  }}
  .doc thead th{{ background:#F1F5F9; font-size:12.5px; color:var(--text-muted); }}
  .doc tbody tr:last-child td{{ border-bottom:none; }}
  .doc code{{
    background:#F1F5F9; border-radius:5px; padding:1px 6px;
    font-size:12.5px;
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  }}
  .doc pre{{
    background:#0F172A; color:#E2E8F0;
    border-radius:10px; padding:14px 16px;
    font-size:12.5px; line-height:1.7;
    overflow-x:auto;
  }}
  .doc pre code{{ background:none; color:inherit; padding:0; }}
  .doc img{{ max-width:100%; height:auto; }}

  footer{{
    text-align:center; font-size:12px; color:var(--text-subtle);
    padding:0 20px 80px;
  }}

  @media (max-width:640px){{
    .topbar{{ padding:10px 14px; gap:10px; }}
    .topbar .file{{ width:100%; margin-left:0; }}
    .doc{{ padding:26px 14px 100px; font-size:14.5px; }}
    .doc h1{{ font-size:21px; }}
    .doc h2{{ font-size:17.5px; margin-top:40px; }}
  }}
</style>
</head>
<body>

<nav class="topbar">
  <span class="kind">原文</span>
  <a href="../">図解に戻る</a>
  <span class="sep">/</span>
  <a href="../../">まとめトップ</a>
  <span class="sep">/</span>
  <a href="../../sources/{md}">Markdown原本</a>
  <span class="file">{md}</span>
</nav>

<article class="doc">
{body}
</article>

<footer>{title} / 原文Markdownをそのまま整形表示したページ</footer>

</body>
</html>
"""


def wrap_tables(fragment: str) -> str:
    """横に長い表がページ幅を割らないよう .table-wrap で包む。"""
    return fragment.replace("<table>", '<div class="table-wrap"><table>').replace(
        "</table>", "</table></div>"
    )


def main() -> int:
    if not SRC_DIR.is_dir():
        print(f"sources/ が無い: {SRC_DIR}", file=sys.stderr)
        return 1

    for doc in DOCS:
        md_path = SRC_DIR / doc["md"]
        if not md_path.is_file():
            print(f"欠落: {md_path}", file=sys.stderr)
            return 1

        proc = subprocess.run(
            ["pandoc", "--from", "gfm", "--to", "html5", str(md_path)],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            print(f"pandoc 失敗 ({doc['md']}): {proc.stderr}", file=sys.stderr)
            return 1

        out_dir = ROOT / doc["slug"] / "source"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "index.html"
        out_path.write_text(
            PAGE.format(
                title=html.escape(doc["title"]),
                accent=doc["accent"],
                md=doc["md"],
                body=wrap_tables(proc.stdout),
            ),
            encoding="utf-8",
        )
        print(f"生成: {out_path.relative_to(ROOT)}  ({out_path.stat().st_size:,} bytes)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
