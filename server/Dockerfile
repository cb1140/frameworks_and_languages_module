FROM python:alpine

EXPOSE 8000

WORKDIR /app/

#install dependancies
RUN pip install gunicorn falcon

COPY . . 

ENTRYPOINT [ "gunicorn","--bind", "0.0.0.0", "app:app" ]

CMD ["python3", "app.py"]