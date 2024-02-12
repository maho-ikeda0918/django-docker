FROM python:3.12-bullseye

# pythonの出力表示をDocker用に調整
ENV PYTHONUNBUFFERD=1

WORKDIR /workspace

RUN pip install poetry

# poetryの定義ファイルをコピー（存在する場合）
COPY pyproject.toml* poetry.lock* ./

# venvのファイルをプロジェクトディレクトリの下に置く（全てのプロジェクトに適用するように）
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# # 開発用サーバー立ち上げ
ENTRYPOINT ["poetry", "run", "python", "project/manage.py", "runserver", "0.0.0.0:8000"]
