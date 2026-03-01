# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# from molscribe import MolScribe
# import os
# import shutil
# from PIL import Image

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"], 
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Путь внутри контейнера (соответствует COPY в Dockerfile)
# MODEL_PATH = "models/model.pth"
# model = None

# # Загружаем модель один раз при старте
# if os.path.exists(MODEL_PATH):
#     model = MolScribe(MODEL_PATH, device='cpu')
# else:
#     print(f"ERROR: Model not found at {MODEL_PATH}")

# @app.get("/")
# def read_root():
#     return {"status": "Backend is running", "model_loaded": model is not None}

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     if model is None:
#         return {"error": "Model not loaded"}

#     temp_path = f"temp_{file.filename}"
#     with open(temp_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     try:
#         # MolScribe возвращает список результатов для каждой картинки
#         results = model.predict_images([temp_path])
#         # Берем SMILES из первого (и единственного) результата
#         smiles_result = results[0]['smiles'] if results else "Not found"
#         return {"smiles": smiles_result}
#     except Exception as e:
#         return {"error": str(e)}
#     finally:
#         if os.path.exists(temp_path):
#             os.remove(temp_path)
# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# from molscribe import MolScribe
# import os
# from PIL import Image
# import io

# app = FastAPI()

# # Настройка CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"], 
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Путь внутри контейнера
# MODEL_PATH = "models/model.pth"
# model = None

# # Загружаем модель один раз при старте
# if os.path.exists(MODEL_PATH):
#     try:
#         model = MolScribe(MODEL_PATH, device='cpu')
#         print("SUCCESS: Model loaded successfully")
#     except Exception as e:
#         print(f"ERROR: Failed to initialize model: {e}")
# else:
#     print(f"ERROR: Model file not found at {MODEL_PATH}")

# @app.get("/")
# def read_root():
#     return {
#         "status": "Backend is running", 
#         "model_loaded": model is not None
#     }

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     if model is None:
#         return {"error": "Model not loaded"}

#     try:
#         # 1. Читаем байты файла
#         file_bytes = await file.read()
        
#         # 2. Открываем через PIL и конвертируем в RGB
#         image = Image.open(io.BytesIO(file_bytes)).convert('RGB')
        
#         # 3. Передаем СПИСОК изображений в аргумент input_images
#         # Исправлено: добавлено
#         results = model.predict_images(input_images=)
        
#         # 4. MolScribe возвращает список словарей
#         if results and len(results) > 0:
#             smiles_result = results[0].get('smiles', "Not found")
#             return {"smiles": smiles_result}
#         else:
#             return {"smiles": "No molecule detected"}

#     except Exception as e:
#         return {"error": f"Prediction failed: {str(e)}"}
#     finally:
#         await file.close()
# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# from molscribe import MolScribe
# import os
# from PIL import Image
# import io

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"], 
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# MODEL_PATH = "models/model.pth"
# model = None

# if os.path.exists(MODEL_PATH):
#     try:
#         model = MolScribe(MODEL_PATH, device='cpu')
#         print("SUCCESS: Model loaded successfully")
#     except Exception as e:
#         print(f"ERROR: Failed to initialize model: {e}")
# else:
#     print(f"ERROR: Model file not found at {MODEL_PATH}")

# @app.get("/")
# def read_root():
#     return {"status": "Backend is running", "model_loaded": model is not None}

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     if model is None:
#         return {"error": "Model not loaded"}

#     try:
#         # Читаем картинку из запроса
#         file_bytes = await file.read()
#         image = Image.open(io.BytesIO(file_bytes)).convert('RGB')
        
#         # Исправлено: передаем список в аргумент input_images
#         results = model.predict_images(input_images=)
        
#         # MolScribe возвращает список словарей. Берем первый элемент.
#         if results and len(results) > 0:
#             smiles_result = results[0].get('smiles', "Not found")
#             return {"smiles": smiles_result}
#         else:
#             return {"smiles": "No molecule detected"}

#     except Exception as e:
#         return {"error": f"Prediction failed: {str(e)}"}
#     finally:
#         await file.close()
# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# from molscribe import MolScribe
# import os
# from PIL import Image
# import io

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"], 
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# MODEL_PATH = "models/model.pth"
# model = None

# if os.path.exists(MODEL_PATH):
#     try:
#         model = MolScribe(MODEL_PATH, device='cpu')
#         print("SUCCESS: Model loaded successfully")
#     except Exception as e:
#         print(f"ERROR: Failed to initialize model: {e}")
# else:
#     print(f"ERROR: Model file not found at {MODEL_PATH}")

# @app.get("/")
# def read_root():
#     return {"status": "Backend is running", "model_loaded": model is not None}

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     if model is None:
#         return {"error": "Model not loaded"}

#     try:
#         file_bytes = await file.read()
#         image = Image.open(io.BytesIO(file_bytes)).convert('RGB')
        
#         # --- ЛОГИРОВАНИЕ ДЛЯ ПРОВЕРКИ ---
#         print(f"DEBUG: Received file: {file.filename}")
#         print(f"DEBUG: Image size: {image.size}")  # Поймем разрешение
#         print(f"DEBUG: Image mode: {image.mode}")  # Должно быть RGB
        
#         # Пробуем отправить изображение
#         # MolScribe часто возвращает список словарей. Проверим его структуру.
#         results = model.predict_images(input_images=)
        
#         print(f"DEBUG: Raw results from model: {results}") 
#         # -------------------------------

#         # Важный момент: MolScribe возвращает список: [{'smiles': '...', ...}]
#         if isinstance(results, list) and len(results) > 0:
#             smiles_result = results[0].get('smiles', "SMILES key not found")
#             return {"smiles": smiles_result}
#         else:
#             return {"error": "Unexpected results format", "raw": str(results)}

#     except Exception as e:
#         print(f"DEBUG ERROR: {str(e)}")
#         return {"error": f"Prediction failed: {str(e)}"}
#     finally:
#         await file.close()
# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# from molscribe import MolScribe
# import os
# from PIL import Image
# import io
# import numpy as np

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"], 
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# MODEL_PATH = "models/model.pth"
# model = None

# if os.path.exists(MODEL_PATH):
#     try:
#         model = MolScribe(MODEL_PATH, device='cpu')
#         print("SUCCESS: Model loaded successfully")
#     except Exception as e:
#         print(f"ERROR: Failed to initialize model: {e}")
# else:
#     print(f"ERROR: Model file not found at {MODEL_PATH}")

# @app.get("/")
# def read_root():
#     return {"status": "Backend is running", "model_loaded": model is not None}

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     if model is None:
#         return {"error": "Model not loaded"}

#     try:
#         file_bytes = await file.read()
#         # 1. Читаем изображение
#         img = Image.open(io.BytesIO(file_bytes)).convert('RGB')
        
#         # 2. Оборачиваем в список, так как MolScribe работает с пачками (batches)
#         # И передаем именно этот список в модель
#         results = model.predict_images(input_images=[img])
        
#         # 3. Обработка результата
#         if isinstance(results, list) and len(results) > 0:
#             # MolScribe возвращает список словарей, берем первый
#             smiles_value = results[0].get('smiles', "Not found")
#             return {"smiles": smiles_value}
#         else:
#             return {"smiles": "No molecule found", "debug": str(results)}

#     except Exception as e:
#         return {"error": f"Prediction failed: {str(e)}"}
#     finally:
#         await file.close()
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from molscribe import MolScribe
import os
from PIL import Image
import io
import numpy as np

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Путь к модели внутри контейнера
MODEL_PATH = os.getenv("MODEL_PATH", "models/model.pth")
model = None

# Инициализация модели при запуске
# if os.path.exists(MODEL_PATH):
#     try:
#         # MolScribe может требовать device='cpu' в Docker без GPU
#         if os.path.exists(MODEL_PATH):
#     try:
#         import torch
#         device = 'cuda' if torch.cuda.is_available() else 'cpu'
#         model = MolScribe(MODEL_PATH, device=device)
#         print(f"SUCCESS: Model loaded on {device.upper()}")
#     except Exception as e:
#         print(f"ERROR: {e}")
#         print(f"SUCCESS: Model loaded successfully from {MODEL_PATH}")
#     except Exception as e:
#         print(f"ERROR: Failed to initialize model: {e}")
# else:
#     print(f"ERROR: Model file not found at {MODEL_PATH}. Check your docker-compose volumes.")
if os.path.exists(MODEL_PATH):
    try:
        import torch
        # Явно создаем объект device
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = MolScribe(MODEL_PATH, device=device)
        print(f"SUCCESS: Model loaded on {device}")
    except Exception as e:
        print(f"ERROR: Failed to initialize model: {e}")
else:
    print(f"ERROR: Model file not found at {MODEL_PATH}")
    
@app.get("/")
def read_root():
    return {
        "status": "Backend is running", 
        "model_loaded": model is not None,
        "model_path": MODEL_PATH
    }

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if model is None:
        return {"error": "Model not loaded on server. Check logs."}

    try:
        # 1. Читаем байты файла
        file_bytes = await file.read()
        
        # 2. Открываем через PIL и конвертируем в RGB
        pil_image = Image.open(io.BytesIO(file_bytes)).convert('RGB')
        
        # 3. Важно: Конвертируем PIL Image в Numpy Array (решает вашу ошибку из логов)
        image_np = np.array(pil_image)
        
        # 4. Вызываем модель. Передаем список [image_np]
        # MolScribe возвращает список словарей
        results = model.predict_images(input_images=[image_np])
        
        # 5. Обработка результата
        if isinstance(results, list) and len(results) > 0:
            # Берём первый элемент (так как отправляли одну картинку)
            prediction = results[0]
            smiles_value = prediction.get('smiles', "Not found")
            
            return {
                "smiles": smiles_value,
                "confidence": prediction.get('smiles_prob', None)
            }
        else:
            return {"smiles": "No molecule found", "debug": str(results)}

    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}
    finally:
        await file.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)