"""
定期実行用：おもちゃ最安値比較記事を自動生成
"""

import random
from generate_article import create_post

# 人気おもちゃ・比較キーワード
TOPICS = [
    ("{item} 最安値比較｜Amazon・楽天・Yahoo!どこが安い？【{year}年{month}月】",
     "価格比較", "Amazonで最安値をチェック"),

    ("【{year}年】{item} のおすすめ{num}選｜{age}歳向け人気ランキング",
     "おすすめランキング", "人気商品をAmazonで見る"),

    ("{item} は何歳から？特徴・価格・口コミまとめ",
     "おもちゃ解説", "Amazonで価格を確認する"),

    ("誕生日プレゼントに{item}｜{age}歳の子供に喜ばれる理由",
     "プレゼント", "ギフトラッピングでAmazonから贈る"),

    ("{item} セール情報まとめ｜最安値で買うベストタイミング",
     "セール情報", "Amazonタイムセールをチェック"),
]

ITEMS = [
    "レゴ クラシック", "シルバニアファミリー", "プラレール", "トミカ",
    "アンパンマン おもちゃ", "ニンテンドースイッチ ソフト", "ベイブレード",
    "リカちゃん", "人生ゲーム", "ジェンガ", "UNO", "ドラえもん おもちゃ",
    "鬼滅の刃 フィギュア", "ポケモン カードゲーム", "ミニオン ぬいぐるみ",
]

FILLERS = {
    "year": ["2026"],
    "month": ["6", "7", "8", "9"],
    "num": ["5", "7", "10"],
    "age": ["3", "4", "5", "6", "7", "8"],
}

def pick_topic():
    template, category, cta = random.choice(TOPICS)
    item = random.choice(ITEMS)
    title = template.replace("{item}", item)
    for key, values in FILLERS.items():
        placeholder = f"{{{key}}}"
        if placeholder in title:
            title = title.replace(placeholder, random.choice(values), 1)
    return title, category, cta

if __name__ == "__main__":
    title, category, cta_text = pick_topic()
    print(f"生成テーマ: {title} [{category}]")
    create_post(title, category, cta_text=cta_text, cta_url="")
