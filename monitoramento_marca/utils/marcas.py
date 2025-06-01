import json
from pathlib import Path

def carregar_palavras_chave(caminho="utils/palavras_chave.json") -> dict:
    caminho_json = Path(caminho)
    if not caminho_json.exists():
        raise FileNotFoundError(f"Arquivo de palavras-chave não encontrado: {caminho}")

    with open(caminho_json, "r", encoding="utf-8") as f:
        return json.load(f)
