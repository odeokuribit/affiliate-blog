"""
テンプレートベース記事生成スクリプト（API不要・完全無料）
使い方: python generate_article.py "商品名" "カテゴリ" [CTA文章] [CTAリンク]
"""

import sys
import random
from datetime import datetime


def slugify(title: str) -> str:
    import re, hashlib
    # 英数字とハイフンのみ残す
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[\s_-]+', '-', slug).strip('-')
    # 日本語しかない場合はハッシュで短縮
    if not re.search(r'[a-z0-9]', slug):
        slug = "post-" + hashlib.md5(title.encode()).hexdigest()[:8]
    return slug[:50] or "article"


def generate_price_comparison_article(product: str) -> str:
    prices = {
        "amazon": random.randint(1800, 4500),
        "rakuten": random.randint(1900, 4800),
        "yahoo": random.randint(1750, 4600),
    }
    min_shop = min(prices, key=prices.get)
    shop_names = {"amazon": "Amazon", "rakuten": "楽天市場", "yahoo": "Yahoo!ショッピング"}

    amazon_p = f"¥{prices['amazon']:,}"
    rakuten_p = f"¥{prices['rakuten']:,}"
    yahoo_p = f"¥{prices['yahoo']:,}"
    min_price = f"¥{prices[min_shop]:,}"
    min_name = shop_names[min_shop]

    return f"""
## {product} 最安値まとめ（{datetime.now().strftime('%Y年%m月')}時点）

| ショップ | 価格（税込） | 送料 | ポイント |
|---|---|---|---|
| Amazon | {amazon_p} | 無料（Prime） | なし |
| 楽天市場 | {rakuten_p} | 無料 | あり |
| Yahoo!ショッピング | {yahoo_p} | 無料 | PayPayポイント |

> **最安値：{min_name} {min_price}**

---

## {product} の特徴

{product}は赤ちゃん・幼児に人気のおもちゃです。

- **対象年齢**：1歳〜6歳
- **安全基準**：日本玩具協会安全基準適合
- **特徴**：カラフルで子供の好奇心を刺激する設計

誕生日プレゼントやクリスマスギフトとして毎年人気です。

---

## どこで買うのが一番お得？

### Amazon の特徴
- Primeなら**翌日配送**対応
- ギフトラッピングオプションあり
- タイムセール時にさらに安くなることも

### 楽天市場の特徴
- **お買い物マラソン**でポイント還元が大きくなる
- 5のつく日・0のつく日がねらい目
- 楽天カード利用でさらにお得

### Yahoo!ショッピングの特徴
- **PayPayポイント**が貯まる
- 日曜日はポイント還元率アップ
- ソフトバンクユーザーはさらにお得

---

## 価格が安くなるタイミング

| 時期 | セール名 | 割引率の目安 |
|---|---|---|
| 11月 | Amazonブラックフライデー | 20〜30%OFF |
| 12月 | クリスマスセール | 10〜20%OFF |
| 1月 | 新春セール | 10〜15%OFF |
| 誕生月 | 各サイトクーポン | 5〜10%OFF |

クリスマス前（11〜12月）は在庫切れになりやすいため、**早めの購入がおすすめ**です。

---

## まとめ

- **今すぐ欲しい**→ Amazon（即日〜翌日配送）
- **ポイントを貯めたい**→ 楽天（マラソン期間中）
- **PayPayユーザー**→ Yahoo!ショッピング

価格は毎日変動するため、購入前に必ず各サイトで最新価格をご確認ください。
"""


def generate_ranking_article(product: str, category: str) -> str:
    items = [
        f"{product} プレミアム",
        f"{product} スタンダード",
        f"{product} ミニ",
        f"{product} デラックス",
        f"{product} ベーシック",
    ]
    return f"""
## {category}の選び方

{category}を選ぶときのポイントは以下の3つです。

1. **対象年齢**：お子様の年齢に合ったものを選ぶ
2. **安全性**：STマーク（日本玩具協会）付きを選ぶ
3. **価格**：予算に合わせてコスパの良いものを選ぶ

---

## おすすめランキング TOP5

### 1位：{items[0]}

最も人気が高く、Amazonでベストセラー1位を獲得。対象年齢1歳〜で安心して使えます。

**価格目安：¥2,500〜¥3,500**

### 2位：{items[1]}

コスパ抜群で初めてのおもちゃにおすすめ。シンプルな設計で長く使えます。

**価格目安：¥1,800〜¥2,800**

### 3位：{items[2]}

コンパクトサイズで持ち運びに便利。お出かけや旅行にも最適です。

**価格目安：¥1,500〜¥2,200**

### 4位：{items[3]}

豪華なセット内容で誕生日プレゼントに最適。子供が喜ぶ充実した内容です。

**価格目安：¥3,500〜¥5,000**

### 5位：{items[4]}

シンプルで使いやすく、初めて購入する方におすすめのエントリーモデルです。

**価格目安：¥1,200〜¥1,800**

---

## まとめ

{category}は対象年齢・安全性・価格のバランスで選ぶことが大切です。
迷ったら**1位の{items[0]}**がおすすめです。Amazonでの口コミ評価も高く、多くの親御さんに選ばれています。
"""


def create_post(title: str, category: str, cta_text: str = "", cta_url: str = ""):
    today = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(title)
    filename = f"_posts/{today}-{slug}.md"

    if "最安値" in title or "比較" in title:
        product = title.split("最安値")[0].split("比較")[0].strip().rstrip("　 ")
        content = generate_price_comparison_article(product)
    else:
        content = generate_ranking_article(title, category)

    description = f"{title}。{'・'.join(['Amazon', '楽天', 'Yahoo!'])}の価格を比較してお得な購入先をご紹介します。"[:120]

    frontmatter = f"""---
layout: post
title: "{title}"
date: {today}
categories: [{category}]
description: "{description}"
"""
    if cta_text and cta_url:
        frontmatter += f'cta_text: "{cta_text}"\ncta_url: "{cta_url}"\n'
    frontmatter += "---\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(frontmatter + content)

    print(f"✅ 記事を作成しました: {filename}")
    return filename


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('使い方: python generate_article.py "タイトル" "カテゴリ" [CTA文章] [CTAリンク]')
        sys.exit(1)

    title = sys.argv[1]
    category = sys.argv[2]
    cta_text = sys.argv[3] if len(sys.argv) > 3 else ""
    cta_url = sys.argv[4] if len(sys.argv) > 4 else ""

    create_post(title, category, cta_text, cta_url)
