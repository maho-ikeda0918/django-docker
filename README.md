# Django環境構築
## 1. リモートリポジトリをclone
ブランチ`django-practice-01`のリモートリポジトリをcloneする。

※ブランチに注意すること

```bash
git clone -b django-practice-01 <リモートリポジトリ>
```

## 2. .envの準備
`.env.sample`をコピーして`.env`を作成

.envの中身

```bash
MYSQL_DATABASE=django
MYSQL_USER=django
MYSQL_PASSWORD=secret
MYSQL_ROOT_PASSWORD=root
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

マイグレーション実施

```bash
python manage.py migrate
```

コンテナを出る

```bash
exit
```

## 4. コンテナを再起動

```bash
docker compose restart
```
