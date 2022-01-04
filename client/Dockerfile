#FROM nginx:alpine

#ENV PATH_NGINX_SERVE=/usr/share/nginx/html

#RUN curl https://unpkg.com/vue@next -L -o ${PATH_NGINX_SERVE}/vue.js

#COPY . ${PATH_NGINX_SERVE}

FROM python:alpine

WORKDIR /app/

EXPOSE 8001

COPY . .

CMD ["python3", "-m", "http.server", "8001"]