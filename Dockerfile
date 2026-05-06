# Базовый образ Python
FROM python:3.11-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем код приложения
COPY . .

# Команда запуска
CMD ["python", "app.py"]
