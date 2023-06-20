FROM python:3.8

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh
#CMD ["/app/docker/celery.sh"]
CMD python main.py