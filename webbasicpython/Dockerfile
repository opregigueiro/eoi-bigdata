FROM python:alpine

COPY . /webapp

WORKDIR /webapp

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"] 
