"""
定期実行用：収益性の高いテーマから自動でお題を選んで記事生成
"""

import random
from generate_article import create_post

# 高収益ジャンル（単価が高いカテゴリを優先）
TOPICS = [
    # (タイトルテンプレート, カテゴリ, CTA文章)
    ("おすすめ{item}比較【{year}年】初心者でも失敗しない選び方", "クレジットカード",
     "今すぐ無料で申し込む"),
    ("{item}のおすすめランキング{num}選｜{year}年最新版", "転職",
     "まずは無料登録してスカウトを待つ"),
    ("【体験談】{item}を使って{month}ヶ月で{result}した話", "副業",
     "無料で始める"),
    ("{item}と{item2}を徹底比較！どちらがお得？", "保険",
     "無料で一括見積もりする"),
    ("初心者向け{item}の始め方｜{year}年版完全ガイド", "投資",
     "口座開設（無料）はこちら"),
]

FILLERS = {
    "item": ["クレジットカード", "格安SIM", "転職サービス", "副業", "ネット証券", "医療保険"],
    "item2": ["楽天カード", "PayPayカード", "イオンカード"],
    "year": ["2026"],
    "month": ["3", "6"],
    "num": ["5", "7", "10"],
    "result": ["月5万円稼げた", "転職成功した", "年収100万円上がった"],
    "result2": [""],
}

def pick_topic():
    template, category, cta = random.choice(TOPICS)
    title = template
    for key, values in FILLERS.items():
        placeholder = f"{{{key}}}"
        if placeholder in title:
            title = title.replace(placeholder, random.choice(values), 1)
    return title, category, cta

if __name__ == "__main__":
    title, category, cta_text = pick_topic()
    print(f"生成テーマ: {title} [{category}]")
    create_post(title, category, cta_text=cta_text, cta_url="")
