FROM python:3.10-slim-buster

COPY . /app

WORKDIR /app

RUN apt-get -y update
RUN apt-get -y install git
RUN pip install -r requirements.txt

EXPOSE 5050

CMD ["gunicorn", "--bind", "0.0.0.0:5050", "--timeout", "0", "app:app"]