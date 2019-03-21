FROM python:2.7-alpine

WORKDIR /app

COPY app.py \ 
    requirements.txt \
    README.md LICENSE \
    /app/

RUN pip install -r requirements.txt

CMD ["python", "app.py"]