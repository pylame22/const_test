FROM python:3.10

COPY ./requirements.txt /requirements.txt

RUN mkdir /app

RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY ./deploy/start.sh /start.sh
RUN chmod +x /start.sh

COPY ./app /app
WORKDIR /app/

CMD ["/start.sh"]
