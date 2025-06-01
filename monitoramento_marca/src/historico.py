# src/historico.py
import json
import pandas as pd
from pathlib import Path

REL_DIR = Path("relatorios")        # onde salvamos os .json no monitoramento

def carregar_historico(marca: str | None = None) -> pd.DataFrame:
    """
    Lê todos os arquivos JSON em relatorios/ e devolve um DataFrame.
    Se 'marca' for informada, devolve apenas as menções dessa marca.
    """
    registros: list[dict] = []

    # varre todos os .json gerados
    for arq in REL_DIR.glob("*.json"):
        with open(arq, encoding="utf-8") as f:
            registros.extend(json.load(f))

    if not registros:
        return pd.DataFrame(columns=["marca", "mencao", "sentimento", "data"])

    df = pd.DataFrame(registros)

    # filtra por marca, se necessário
    if marca:
        df = df[df["marca"].str.lower() == marca.lower()]

    return df.reset_index(drop=True)
