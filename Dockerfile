FROM python:3.6.1-alpine

WORKDIR /141_bot_root

ENV TZ 'Asia/Tehran'
RUN apk update && apk add tzdata libpq postgresql-dev build-base jpeg-dev&& \
    pip install --upgrade pip && \
    cp /usr/share/zoneinfo/Asia/Tehran /etc/localtime && \
    echo $TZ > /etc/timezone

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./ ./
CMD ["python", "bot/main_bot.py"]
ENV PYTHONPATH /141_bot_root
