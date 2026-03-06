
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