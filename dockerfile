# Укажите базовый образ
FROM python:3.9

# Установите зависимости
RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# Копирование кода в контейнер
COPY . .

CMD [ "gunicorn", "router:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]
