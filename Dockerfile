FROM python-3.7.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg 

CMD ["python3","main.py"]