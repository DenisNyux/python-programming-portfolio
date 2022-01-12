FROM python:3.9.7-slim

EXPOSE 9000

WORKDIR /home/app

COPY index.html .

CMD ["python3", "-m", "http.server", "9000"]