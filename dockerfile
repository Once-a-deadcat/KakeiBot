# Dockerfile

# Pythonイメージの指定
FROM python:3.10

# 作業ディレクトリを設定
WORKDIR /app

# PYTHONPATHにモジュールのパスを追加
ENV PYTHONPATH="/app:${PYTHONPATH}"

# Pipfileをコピー
COPY Pipfile ./

# pipenvのインストール
RUN pip install pipenv

# Pipfile.lockを作成 (Pipfile.lockがある場合は上書きされない) 
RUN pipenv lock

# パッケージのインストール
RUN pipenv install --system --deploy

# スクリプトとその他のファイルをコピー
COPY . .

# スクリプトを実行
CMD [ "python", "./DiscordBot.py" ]
