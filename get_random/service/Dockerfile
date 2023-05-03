FROM python:alpine

COPY src /webapp

WORKDIR /webapp

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]

