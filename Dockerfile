FROM python:2.7.16

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3","apiCreation.py"]