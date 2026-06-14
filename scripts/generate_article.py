"""
記事自動生成スクリプト
使い方: python generate_article.py "記事タイトル" "カテゴリ"
必要: pip install google-generativeai python-frontmatter
"""

import sys
import os
import re
from datetime import datetime

try:
    import google.generativeai as genai
except ImportError:
    print("pip install google-generativeai を実行してください")
    sys.exit(1)

# Gemini API キー（GitHub Secretsから取得 or 直接入力）
API_KEY = os.environ.get("GEMINI_API_KEY", "")
if not API_KEY:
    print("環境変数 GEMINI_API_KEY を設定してください")
    print("取得先: https://aistudio.google.com/app/apikey （無料）")
    sys.exit(1)

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")  # 無料枠あり


def slugify(title: str) -> str:
    # 日本語タイトルをスラッグ化
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[\s_-]+', '-', slug)
    return slug[:50] or "article"


def generate_article(title: str, category: str) -> str:
    prompt = f"""
あなたはSEOに強い日本語アフィリエイトブログのライターです。
以下の条件で記事を書いてください。

タイトル: {title}
カテゴリ: {category}

条件:
- Jekyll Markdown形式（frontmatterなし、本文のみ）
- 見出しはh2(##)とh3(###)を使う
- 2000〜3000文字
- 読者の悩みを解決する実用的な内容
- 自然な形でアフィリエイトリンク設置を促す文章を含める
- 最後に「まとめ」セクションを設ける
- 表やリストを積極的に使う

記事本文のみ出力してください（frontmatterは不要）:
"""
    response = model.generate_content(prompt)
    return response.text


def create_post(title: str, category: str, cta_text: str = "", cta_url: str = ""):
    today = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(title)
    filename = f"_posts/{today}-{slug}.md"

    content = generate_article(title, category)

    # description生成（1文）
    desc_prompt = f"次のタイトルの記事のmeta descriptionを日本語で1文（120文字以内）で書いてください: {title}"
    description = model.generate_content(desc_prompt).text.strip()

    frontmatter = f"""---
layout: post
title: "{title}"
date: {today}
categories: [{category}]
description: "{description}"
"""
    if cta_text and cta_url:
        frontmatter += f'cta_text: "{cta_text}"\ncta_url: "{cta_url}"\n'
    frontmatter += "---\n\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(frontmatter + content)

    print(f"✅ 記事を作成しました: {filename}")
    return filename


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("使い方: python generate_article.py \"タイトル\" \"カテゴリ\" [CTA文章] [CTAリンク]")
        print('例: python generate_article.py "おすすめクレジットカード5選" "クレカ" "詳しくはこちら" "https://example.com"')
        sys.exit(1)

    title = sys.argv[1]
    category = sys.argv[2]
    cta_text = sys.argv[3] if len(sys.argv) > 3 else ""
    cta_url = sys.argv[4] if len(sys.argv) > 4 else ""

    create_post(title, category, cta_text, cta_url)
