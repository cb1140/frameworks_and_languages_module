FROM alpine
RUN npm install -g @vue/cli
COPY vue.html .
CMD ["python3", "-m", "http.server", "8001"]
