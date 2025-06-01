import pandas as pd
from datetime import datetime
from utils.lista_encadeada import ListaEncadeada, Node
from utils.tradutor import traduzir_pt
from utils.marcas import carregar_palavras_chave
from src.analise_sentimento import analisar_sentimento


def coletar_avaliacoes_dataset(
        marca: str,
        caminho_csv: str = "src/datasets/avaliacoes_amazon.csv",
        limite: int = 20
) -> ListaEncadeada:

    # 1. Carrega o CSV e padroniza nomes de colunas
    df = pd.read_csv(caminho_csv)
    df = df.rename(columns={
        "sentimento": "sentiment",
        "texto": "text"
    })

    # 2. Validação
    if {"sentiment", "text"}.issubset(df.columns) is False:
        raise ValueError("CSV precisa conter colunas 'sentiment' e 'text'.")

    # 3. Carrega palavras-chave relacionadas à marca
    palavras_chave = carregar_palavras_chave()
    palavras_marca = palavras_chave.get(marca.capitalize(), [])

    # 4. Filtra textos que contenham a marca ou palavras relacionadas
    def contem_palavra_chave(texto: str) -> bool:
        texto = texto.lower()
        return any(p.lower() in texto for p in [marca] + palavras_marca)

    df_filtrado = df[df["text"].apply(lambda t: contem_palavra_chave(str(t)))]

    # 5. Se não encontrar nada, usa amostragem aleatória
    if df_filtrado.empty:
        print(f"Nenhuma menção direta ou relacionada à marca '{marca}' encontrada — usando amostra aleatória.")
        df_filtrado = df.sample(n=limite, random_state=42)
    else:
        df_filtrado = df_filtrado.sample(n=min(limite, len(df_filtrado)), random_state=42)

    lista = ListaEncadeada()

    # 6. Processa cada menção
    for _, row in df_filtrado.iterrows():
        texto_en = row["text"]
        sentimento = analisar_sentimento(texto_en)
        texto_pt = traduzir_pt(texto_en)

        registro = {
            "marca": marca,
            "mencao": texto_pt,
            "sentimento": sentimento,
            "data": datetime.now().strftime("%Y-%m-%d")
        }
        lista.inserir(Node(registro))

    return lista

