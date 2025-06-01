# src/analise_sentimento.py
from textblob import TextBlob

def analisar_sentimento(texto: str) -> str:
    """
    Retorna: 'positivo' | 'negativo' | 'neutro'
    Regra simples baseada na polaridade do TextBlob.
    """
    if not texto:
        return "neutro"

    polaridade = TextBlob(texto).sentiment.polarity

    if polaridade > 0.05:
        return "positivo"
    elif polaridade < -0.05:
        return "negativo"
    return "neutro"
