FROM python:3.12

WORKDIR /flask-aplication

COPY ./requirements.txt .

RUN apt-get update && apt-get upgrade
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", 'Flask/main.py']