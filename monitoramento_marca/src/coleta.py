from src.coleta_dataset import coletar_avaliacoes_dataset
from utils.lista_encadeada import ListaEncadeada

def coletar(marca: str, fonte: str = "dataset") -> ListaEncadeada:
    if fonte == "dataset":
        return coletar_avaliacoes_dataset(marca)
    return ListaEncadeada()   # lista vazia para outras fontes
