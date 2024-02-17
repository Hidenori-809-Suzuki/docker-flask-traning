FROM python:3.11-slim

RUN apt-get update && apt-get install -y gcc

WORKDIR /usr/src/app

COPY ./app/requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./app ./

# CMDを修正し、Flaskアプリが正しく実行されるようにする
CMD [ "flask", "run", "--host=0.0.0.0" ]
