FROM python:alpine

COPY . /webapp

WORKDIR /webapp

RUN pip install -qq --trusted-host files.pythonhosted.org -r requirements.txt

ENTRYPOINT ["python", "app.py"] 
