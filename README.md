# Django環境構築
## 1. リモートリポジトリをclone
ブランチ`nginx-django`のリモートリポジトリをcloneする。

※ブランチに注意すること

```bash
git clone -b nginx-django <リモートリポジトリ>
```

## 2. コンテナを作成&起動

```bash
docker compose up -d
```

## 3. Djangoのプロジェクトフォルダ作成
appコンテナへ入る

```bash
docker compose exec app bash
```

プロジェクトフォルダ`app`を作成

```bash
django-admin startproject app .
```

コンテナを出る

```bash
exit
```

## 4. コンテナを再起動

```bash
docker compose restart
```
