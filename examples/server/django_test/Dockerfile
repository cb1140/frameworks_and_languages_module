FROM python:slim

WORKDIR /app/

RUN pip install \
    django

COPY . .

RUN ["python3", "mysite/manage.py", "migrate"]

CMD ["python3", "mysite/manage.py", "runserver", "0.0.0.0:8000"]
