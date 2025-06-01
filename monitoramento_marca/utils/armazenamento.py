# utils/armazenamento.py

import csv
import json
from pathlib import Path
from utils.lista_encadeada import ListaEncadeada

def salvar_json_csv(lista: ListaEncadeada, nome_arquivo: str = "relatorio_mencoes") -> None:
    dados = lista.para_lista()

    # Cria a pasta de saída se necessário
    out_dir = Path("relatorios")
    out_dir.mkdir(exist_ok=True)

    # Caminhos dos arquivos
    caminho_json = out_dir / f"{nome_arquivo}.json"
    caminho_csv = out_dir / f"{nome_arquivo}.csv"

    # Salva em JSON
    with open(caminho_json, "w", encoding="utf-8") as f_json:
        json.dump(dados, f_json, ensure_ascii=False, indent=2)

    # Salva em CSV
    if dados:
        with open(caminho_csv, "w", newline="", encoding="utf-8") as f_csv:
            writer = csv.DictWriter(f_csv, fieldnames=dados[0].keys())
            writer.writeheader()
            writer.writerows(dados)

    print(f"✅ Arquivos salvos em: {caminho_json} e {caminho_csv}")
