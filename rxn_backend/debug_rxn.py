import os
import torch
import json
from rxnscribe import RxnScribe

# Настройка путей внутри контейнера
CKPT_PATH = "models/pix2seq_reaction_full.ckpt"
INPUT_IMG = "data/test.png"  # Если файл лежит в rxn_backend/data/test.png
OUTPUT_JSON = "results/output.json"

def run_debug():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"[*] Работаем на: {device}")

    if not os.path.exists(CKPT_PATH):
        print(f"[!] Файл весов не найден: {CKPT_PATH}")
        return

    print(f"[*] Загрузка модели...")
    model = RxnScribe(CKPT_PATH, device=torch.device('cpu'))

    if os.path.exists(INPUT_IMG):
        print(f"[*] Анализ изображения {INPUT_IMG}...")
        # molscribe=False (только схемы), ocr=True (текст над стрелками)
        results = model.predict_image_file(INPUT_IMG, molscribe=False, ocr=True)
        
        os.makedirs("/app/results", exist_ok=True)
        with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        print(f"[+] Готово! Результат сохранен в results/output.json")
    else:
        print(f"[!] Картинка {INPUT_IMG} не найдена в папке data/")

if __name__ == "__main__":
    run_debug()
