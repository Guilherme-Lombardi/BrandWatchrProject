from src.coleta import coletar
from utils.graficos import gerar_grafico_pizza
from utils.armazenamento import salvar_json_csv

def monitorar_marca(nome_marca: str):
    lista = coletar(nome_marca, fonte="dataset")
    if len(lista) == 0:
        return "Nenhuma menção encontrada.", None

    img = gerar_grafico_pizza(lista, nome_marca)
    salvar_json_csv(lista, nome_marca)

    return f"{len(lista)} menções simuladas para '{nome_marca}'.", img
