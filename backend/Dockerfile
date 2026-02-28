# # Используем легковесный образ с Python
# FROM python:3.9-slim

# # Устанавливаем системные зависимости для RDKit и обработки изображений
# RUN apt-get update && apt-get install -y \
#     libxrender1 \
#     libxext6 \
#     libsm6 \
#     libfontconfig1 \
#     libgl1 \
#     libglib2.0-0 \
#     && rm -rf /var/lib/apt/lists/*

# WORKDIR /app

# # Копируем зависимости и устанавливаем их
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Копируем код и папку с моделью
# COPY app.py .
# # COPY models/ ./models/

# # Открываем порт 8000
# EXPOSE 8000

# # Запуск сервера
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# Python 3.9 подходит, так как MolScribe требует >=3.7
FROM python:3.9-slim

# 1. Системные зависимости (оставляем ваши + чистим кэш)
RUN apt-get update && apt-get install -y \
    libxrender1 \
    libxext6 \
    libsm6 \
    libfontconfig1 \
    libgl1 \
    libglib2.0-0 \
    # Добавляем git, так как некоторые зависимости MolScribe ставятся напрямую с GitHub
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. Установка конкретных версий torch и torchvision
# Если нужен GPU, замените индекс на https://download.pytorch.org
RUN pip install --no-cache-dir \
    torch==1.13.1 \
    torchvision==0.14.1 \
    --extra-index-url https://download.pytorch.org

# 3. Копируем и устанавливаем остальные зависимости
COPY requirements.txt .
# Убедитесь, что в requirements.txt НЕТ строк "torch" и "torchvision", 
# чтобы не перезаписать установленные выше версии
RUN pip install --no-cache-dir -r requirements.txt

# 4. Копируем код
COPY app.py .
# Раскомментируйте, если веса модели лежат локально
# COPY models/ ./models/

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]