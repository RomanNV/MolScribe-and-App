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
# FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu22.04

# # 1. Системные зависимости (оставляем ваши + чистим кэш)
# RUN apt-get update && apt-get install -y \
#     python3.9 \
#     python3-pip \
#     libxrender1 \
#     libxext6 \
#     libsm6 \
#     libgl1 \
#     libglib2.0-0 \
#     git \
#     && rm -rf /var/lib/apt/lists/*
# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
# RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

# WORKDIR /app

# # 2. Установка конкретных версий torch и torchvision
# # Если нужен GPU, замените индекс на https://download.pytorch.org
# RUN pip install --no-cache-dir \
#     torch==1.13.1+cu117 \
#     torchvision==0.14.1+cu117 \
#     --extra-index-url https://download.pytorch.org

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY app.py .

# EXPOSE 8000

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# 1. Используем официальный образ NVIDIA с поддержкой CUDA 11.7 и cuDNN 8
FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu22.04

# 1. Настройка окружения
ENV DEBIAN_FRONTEND=noninteractive
# Устанавливаем PYTHONUNBUFFERED, чтобы логи сразу выводились в консоль Docker
ENV PYTHONUNBUFFERED=1 

# 2. Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    libxrender1 \
    libxext6 \
    libsm6 \
    libgl1 \
    libglib2.0-0 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Создаем символическую ссылку для удобства
RUN ln -s /usr/bin/python3 /usr/bin/python

# КРИТИЧЕСКИЙ ШАГ: Обновляем pip. 
# Это лечит AssertionError и ускоряет расчет зависимостей
RUN pip3 install --upgrade pip

WORKDIR /app

# 3. Установка зависимостей
COPY requirements.txt .

# Мы объединяем установку PyTorch и requirements.
# Используем --extra-index-url, чтобы pip мог брать torch из спец. репозитория NVIDIA/PyTorch,
# а остальные библиотеки (fastapi, transformers и т.д.) — из стандартного PyPI.
RUN pip3 install --no-cache-dir \
    torch==1.13.1+cu117 \
    torchvision==0.14.1+cu117 \
    -r requirements.txt \
    --extra-index-url https://download.pytorch.org/whl/cu117

# 4. Копирование приложения
COPY app.py .

# Открываем порт для FastAPI
EXPOSE 8000

# Запуск сервера
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]