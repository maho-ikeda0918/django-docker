# Django環境構築

**※注意①**

パッケージ管理を`poetry`というツールで行います。

この他にもPythonでは、`pip` `pyenv` `pipenv`など様々なパッケージ管理ツールがあります。

[Pythonのパッケージ管理ツールのコマンド比較表](https://zenn.dev/tanny/articles/041f46c06f76f5)

このリポジトリでは`poetry`を使いますが、現場によって管理の方法は異なるので注意してください。

**※注意②**

手順1~3は、初回だけ行う手順です（git cloneして初回立ち上げ時のみ）。

2回目以降は手順4を行うのみでコンテナを立ち上げることができます。

## 1. poetryインストール
まずはパッケージ管理ツールのインストールをします。

```bash
docker compose run --rm --entrypoint "poetry init --name app --dependency django --dependency mysqlclient" app
```

コマンドを実行すると、色々聞かれるので、以下に倣って入力します。

```bash
This command will guide you through creating your pyproject.toml config.

Version [0.1.0]:                    # <- 何も入力せずEnter
Description []:                     # <- 「Django Practice」と入力
Author [None, n to skip]:           # <- 「n」と入力
License []:                         # <- 何も入力せずEnter
Compatible Python versions [^3.12]: # <- 何も入力せずEnter


Using version ^5.0.2 for django
Would you like to define your main dependencies interactively? (yes/no) [yes] 
You can specify a package in the following forms:
  - A single name (requests): this will search for matches on PyPI
  - A name and a constraint (requests@^2.23.0)
  - A git url (git+https://github.com/python-poetry/poetry.git)
  - A git url with a revision (git+https://github.com/python-poetry/poetry.git#develop)
  - A file path (../my-package/my-package.whl)
  - A directory (../my-package/)
  - A url (https://example.com/packages/my-package-0.1.0.tar.gz)

Package to add or search for (leave blank to skip):  # <- 何も入力せずEnter

Would you like to define your development dependencies interactively? (yes/no) [yes]  # <- 何も入力せずEnter
Package to add or search for (leave blank to skip):  # <- 何も入力せずEnter

Generated file

[tool.poetry]
name = "app"
version = "0.1.0"
description = "Django Practice"
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
django = "^5.0.2"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes]  # <- 何も入力せずEnter
```

入力し終えると`pyproject.toml`ファイルが作成されます。

```toml
# pyproject.toml
[tool.poetry]
name = "app"
version = "0.1.0"
description = "Django Practice"
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
django = "^5.0.2"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
## 2. Djangoインストール

```bash
docker compose run --rm --entrypoint "poetry install --no-root" app
```

コマンドを実行すると、`poetry.lock`ファイルが作成されます。

また、Djangoのインストールも同時にされます。

## 3. プロジェクトを作成する
Djangoのプロジェクトフォルダ`project`を作成します。

```bash
docker compose run --rm --entrypoint "poetry run django-admin startproject project" app
```

プロジェクトフォルダを別名にしたい場合は、`startproject <プロジェクト名>`を変更してください。

## 4. コンテナの作成&起動

```bash
docker compose up -d
```

Djangoの画面が表示されれば起動成功です。

![http://localhost:8002](http://localhost:8002)


### コンテナの停止&削除

```bash
docker compose down
```

### アプリケーションコンテナに入る

```bash
docker compose exec app bash
```

### データベースコンテナに入る

```bash
docker compose exec db bash
```

コンテナから出る

```bash
exit
```

## アプリケーションの作成
Djangoのコマンドは、まず`docker compose exec app bash`でアプリケーションコンテナに入って実行します。

今回はパッケージ管理に`poetry`を使っているので、コマンドの先頭に`poetry run`を付けてコマンド実行します。

**※ここは採用するパッケージ管理ツールによって代わるので注意してください。**

アプリケーション「blogapp」を作成

```bash
poetry run python manage.py startapp blogapp
```

## マイグレーション
DB接続設定やマイグレーションは各自で行ってください。
