# セットアップ手順（30分でできます）

## ステップ1: GitHubアカウント作成（5分）

1. https://github.com にアクセス
2. 「Sign up」でアカウント作成（無料）
3. メール認証を完了

## ステップ2: リポジトリ作成（2分）

1. GitHubにログイン
2. 右上の「+」→「New repository」
3. Repository name: `affiliate-blog`（または好きな名前）
4. **Public** を選択
5. 「Create repository」をクリック

## ステップ3: ファイルをアップロード（5分）

1. リポジトリページで「uploading an existing file」をクリック
2. `affiliate-blog` フォルダの中身を**全て**ドラッグ&ドロップ
   - ※ `.github` フォルダも含める（隠しフォルダに注意）
3. 「Commit changes」をクリック

## ステップ4: GitHub Pages を有効化（2分）

1. リポジトリの「Settings」タブをクリック
2. 左メニュー「Pages」を選択
3. Source: **Deploy from a branch**
4. Branch: **main** / **/ (root)**
5. 「Save」をクリック
6. 数分後に `https://あなたのユーザー名.github.io/affiliate-blog/` で公開！

## ステップ5: Gemini APIキー取得（3分・無料）

1. https://aistudio.google.com/app/apikey にアクセス
2. Googleアカウントでログイン
3. 「Create API key」をクリック
4. キーをコピーしておく

## ステップ6: GitHub SecretsにAPIキーを登録（2分）

1. リポジトリの「Settings」→「Secrets and variables」→「Actions」
2. 「New repository secret」をクリック
3. Name: `GEMINI_API_KEY`
4. Value: 先ほどコピーしたキーを貼り付け
5. 「Add secret」

## ステップ7: A8.net に登録（10分）

1. https://www.a8.net にアクセス
2. 「メディア（サイト運営者）」として登録
3. サイトURLに `https://あなたのユーザー名.github.io/affiliate-blog/` を入力
4. 承認後、アフィリエイトリンクを記事のCTA URLに貼り付ける

---

## 記事を手動で生成する方法

GitHubリポジトリの「Actions」タブ →「記事自動生成・公開」→「Run workflow」
タイトルとカテゴリを入力して実行するだけ！

## 自動投稿スケジュール

週3回（月・水・金 朝9時）に自動で記事を生成・公開します。
スケジュールは `.github/workflows/auto-post.yml` の cron 設定で変更できます。

---

## 費用まとめ

| 項目 | 費用 |
|------|------|
| GitHub Pages | **無料** |
| Gemini API | **無料**（月15リクエスト/分、1日1500リクエスト） |
| A8.net | **無料**（成果報酬のみ） |
| ドメイン | 無料（github.io サブドメイン使用時） |
| **合計** | **¥0/月** |
