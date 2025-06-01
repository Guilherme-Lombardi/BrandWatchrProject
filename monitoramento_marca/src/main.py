import re
import gradio as gr
import pandas as pd
from src.coleta_dataset import coletar_avaliacoes_dataset
from src.historico import carregar_historico
from utils.armazenamento import salvar_json_csv
from utils.graficos import gerar_grafico_pizza

# ------------------- Funções -------------------
def monitorar_marca(marca: str):
    lista = coletar_avaliacoes_dataset(marca)
    salvar_json_csv(lista, marca)
    grafico_path = gerar_grafico_pizza(lista, marca)
    return f"✅ {len(lista)} menções coletadas para '{marca}'.", grafico_path

def acao_analise(marca: str):
    marca_limpa = re.sub(r"[^A-Za-zÀ-ÿ0-9 ]+", "", marca).strip()
    if not marca_limpa or marca_limpa.isnumeric():
        return "❌ Por favor, digite um nome de marca válido (letras ou letras + números).", None
    return monitorar_marca(marca_limpa)

def exibir_historico(marca: str, sentimento: str, ordem: str):
    df = carregar_historico(marca)
    df["data"] = pd.to_datetime(df["data"], errors='coerce')
    df = df.sort_values(by="data", ascending=False)
    df["data"] = df["data"].dt.strftime("%Y-%m-%d")

    # Ordenação conforme escolha
    ascendente = True if ordem == "Mais antigas primeiro" else False
    df = df.sort_values(by="data", ascending=ascendente)

    # Aplica filtro de sentimento
    if sentimento and sentimento != "Todos":
        df = df[df["sentimento"] == sentimento]
    return df

# ------------------- CSS Personalizado -------------------
custom_css = """
.custom-box textarea {
    background-color: #1a1a1d !important;
    border: 1px solid #2e2e32 !important;
    color: white !important;
    border-radius: 10px !important;
}

.custom-btn {
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 20px;
    font-size: 16px;
    box-shadow: 0 0 12px rgba(91, 33, 182, 0.6);
    transition: all 0.3s ease-in-out;
}
.custom-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 0 18px rgba(91, 33, 182, 0.9);
}

footer, .svelte-1ipelgc {
    display: none !important;
}

.gradio-container {
    background-color: #0e0e10 !important;
    color: white;
}

#logo img {
    max-width: 200px;
    margin: 0 auto;
    display: block;
    margin-bottom: 20px;
}

#tabela_historico td {
    white-space: normal !important;
    word-wrap: break-word;
    font-size: 14px;
    padding: 10px;
    color: white;
}

#tabela_historico {
    background-color: #1a1a1d;
    border-radius: 10px;
    overflow-y: auto;
    max-height: 500px;
    border: 1px solid #2e2e32;
    padding: 10px;
    box-shadow: 0 0 12px rgba(255, 255, 255, 0.05);
}

/* Aumentar largura da coluna 'marca' (1ª coluna) */
#tabela_historico th:nth-child(1),
#tabela_historico td:nth-child(1) {
    min-width: 160px;
    max-width: 200px;
}


/* Aumentar largura da coluna 'sentimento' (3ª coluna) */
#tabela_historico th:nth-child(3),
#tabela_historico td:nth-child(3) {
    min-width: 120px;
    max-width: 160px;
}

/* Aumentar largura da coluna 'data' (4ª coluna) */
#tabela_historico th:nth-child(4),
#tabela_historico td:nth-child(4) {
    min-width: 180px;
    max-width: 200px;
}
"""

# ------------------- Tema personalizado -------------------
tema_brandwatchr = gr.themes.Base().set(
    body_background_fill="#0e0e10",
    body_text_color="#ffffff",
    button_primary_background_fill="#3b82f6",
    button_primary_background_fill_hover="#8b5cf6",
    button_primary_text_color="#ffffff",
    button_primary_shadow="0px 0px 10px #3b82f6",
    block_background_fill="#1a1a1d",
    block_border_color="#2e2e32",
    block_shadow="0px 0px 8px #3b82f655"
)

# ------------------- Interface -------------------
with gr.Blocks(theme=tema_brandwatchr, css=custom_css, title="Monitoramento de Marca") as app:
    gr.Image(value="logoImage/logoMarcaProjeto.png", show_label=False, container=False, elem_id="logo")

    with gr.Tab("🔍 Análise de Marca"):
        gr.Markdown("## 🧠 Análise de Marca com IA")
        nome_marca = gr.Textbox(label="Nome da marca", elem_classes="custom-box")
        botao_analisar = gr.Button("Analisar", elem_classes="custom-btn")
        saida_status = gr.Textbox(label="Status", elem_classes="custom-box")
        imagem_grafico = gr.Image(label="Distribuição de sentimentos")

        botao_analisar.click(
            fn=acao_analise,
            inputs=nome_marca,
            outputs=[saida_status, imagem_grafico]
        )

    with gr.Tab("📜 Histórico de Menções"):
        gr.Markdown("## 🕓 Histórico")

        with gr.Row():
            marca_filtro = gr.Textbox(
                label="Filtrar por marca (opcional)",
                elem_classes="custom-box"
            )

            ordem_data = gr.Dropdown(
                choices=["Mais recentes primeiro", "Mais antigas primeiro"],
                value="Mais recentes primeiro",
                label="Ordenar por data",
                elem_classes="custom-box"
            )

            filtro_sentimento = gr.Dropdown(
                choices=["Todos", "positivo", "neutro", "negativo"],
                value="Todos",
                label="Filtrar por sentimento",
                elem_classes="custom-box"
            )

        botao_filtrar = gr.Button(
            "Filtrar",
            elem_classes="custom-btn"
        )

        tabela_historico = gr.Dataframe(
            headers=["marca", "mencao", "sentimento", "data"],
            datatype=["str", "str", "str", "str"],
            row_count=10,
            col_count=(4, "fixed"),
            interactive=False,
            wrap=True,
            type="pandas",
            label="Histórico de Menções",
            elem_id="tabela_historico"
        )

        botao_filtrar.click(
            fn=exibir_historico,
            inputs=[marca_filtro, filtro_sentimento, ordem_data],
            outputs=tabela_historico
        )

# ------------------- Execução -------------------
if __name__ == "__main__":
    app.launch()
