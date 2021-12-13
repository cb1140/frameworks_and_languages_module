FROM alpine
RUN npm install vue
COPY vue.html .
CMD ["python3", "-m", "http.server", "8001"]
