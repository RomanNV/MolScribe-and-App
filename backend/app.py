
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