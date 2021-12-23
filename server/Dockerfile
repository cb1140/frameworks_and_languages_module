FROM python:slim
WORKDIR /app/
#install dependancies
RUN pip install falcon gunicorn
RUN npm install -g npm@8.3.0
COPY . . 
ENTRYPOINT [ "gunicorn","--bind", "0.0.0.0", "sample:app" ]