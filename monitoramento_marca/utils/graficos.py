import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
from pathlib import Path
from utils.lista_encadeada import ListaEncadeada

def gerar_grafico_pizza(lista: ListaEncadeada, nome_marca: str) -> str:
    sentimentos = [n["sentimento"] for n in lista.para_lista()]
    contagem = Counter(sentimentos)

    labels = list(contagem.keys())
    valores = list(contagem.values())

    # Cores fixas por sentimento
    cores_personalizadas = {
        "positivo": "#4CAF50",  # verde
        "negativo": "#F44336",  # vermelho
        "neutro": "#2196F3",    # azul-claro
    }

    cores = [cores_personalizadas.get(label, "#9E9E9E") for label in labels]  # cinza como fallback

    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=labels, colors=cores,
            autopct='%1.1f%%', startangle=140)
    plt.title(f"Distribuição de Sentimentos - {nome_marca.capitalize()}")

    out_dir = Path("graficos")
    out_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    caminho_img = out_dir / f"grafico_{nome_marca}_{timestamp}.png"
    plt.savefig(caminho_img, bbox_inches='tight')
    plt.close()

    return str(caminho_img)
