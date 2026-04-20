import json
import os
import logging
from pathlib import Path

CONFIG_PATH=Path(__file__).resolve().parent.parent / "config" / "config.json"

def load_rules():
    if not CONFIG_PATH.exists():
        print (f"Attenzione,: {CONFIG_PATH} non trovato!")
        return{}
    
    try: 
        with open (CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Errore: il file {CONFIG_PATH} contiene JSON non valido")
        return{}
    

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format=("%(asctime)s - %(levelname)s - %(message)s"),
        handlers=[
            logging.FileHandler("logs/app.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("file_organizer")