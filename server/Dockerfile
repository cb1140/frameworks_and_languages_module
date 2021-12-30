FROM python:alpine

EXPOSE 8000

WORKDIR /app/

RUN pip install gunicorn falcon

RUN npm install -g npm@8.3.0

COPY . . 

ENTRYPOINT [ "gunicorn","--bind", "0.0.0.0", "app:app" ]

CMD ["python3", "app.py"]