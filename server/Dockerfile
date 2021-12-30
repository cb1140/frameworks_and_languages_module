FROM python:slim
WORKDIR /app/
#install dependancies
RUN pip install falcon gunicorn
COPY . . 
ENTRYPOINT [ "gunicorn","--bind", "0.0.0.0", "sample:app" ]