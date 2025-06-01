# 🚀 Nome do Projeto
BrandWatchr

**Resumo:** O BrandWatchr é um aplicativo de monitoramento automatizado que coleta, organiza e analisa menções públicas sobre marcas a partir de datasets reais.Embora não opere em tempo real, fornece às empresas insights valiosos sobre a percepção pública, ajudando na proteção da reputação,identificação de oportunidades de engajamento e planejamento de ações diante de possíveis crises.

---

## 🎯 Objetivo

O BrandWatchr é um sistema desenvolvido para monitorar automaticamente menções públicas sobre marcas, classificando-as por sentimento (positivo, neutro ou negativo). A ferramenta permite que empresas analisem a percepção do público com base em dados coletados previamente, apoiando decisões estratégicas sobre comunicação e marketing.
---

## 👨‍💻 Tecnologias Utilizadas

Liste as principais tecnologias, linguagens, frameworks e bibliotecas utilizadas:

- Python 3.12 
- Gradio / Textblob
- Pandas
- matplotlib
- deep-translator
- GoogleTranslator
- HuggingFace

---

## 🗂️ Estrutura do Projeto

A estrutura a seguir é um exemplo. Vocês devem usar a estrutura do seu projeto obrigatóriamente. 
```
MONITORAMENTO_MARCA/
│
├── .gradio/                   
│
├── build/                     
│   └── main/                  
│
├── graficos/                  
│
├── logomage/                  
│
├── relatorios/                
│
├── src/                       
│   ├── datasets/              
│   │   └── avaliacoes_amazon.csv  
│   │
│   ├── analise_sentimento.py  
│   ├── coleta_dataset.py      
│   ├── coleta.py              
│   ├── historico.py           
│   ├── main.py                
│   ├── monitoramento.py       
│
├── utils/                     
│   ├── armazenamento.py       
│   ├── graficos.py            
│   ├── lista_encadeada.py     
│   ├── marcas.py              
│   ├── palavras_chave.json    
│   └── tradutor.py            
│
├── README.md                  
├── requirements.txt         
```

---

## ⚙️ Como Executar

### ✅ Rodando Localmente

1. Clone o repositório:

```
git clone https://github.com/Guilherme-Lombardi/BrandWatchrProject.git
cd nome-do-projeto
```

2. Crie o ambiente virtual e ative:

```
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

3. Instale as dependências:

```
pip install -r requirements.txt

python -m textblob.download_corpora
```

4. Execute a aplicação:

```
python -m src.main
```

---

## 📸 Demonstrações

Inclua aqui prints, gifs ou vídeos mostrando a interface ou o funcionamento do sistema:

- Tela inicial
  ![Captura de tela 2025-06-01 120320](https://github.com/user-attachments/assets/94110b16-31f0-41b9-a34f-f090fefeafaf)
- Exemplo de funcionalidade</br>

https://github.com/user-attachments/assets/2e19afec-ad88-48d7-806b-1900de7924ee

---

## 👥 Equipe

| Nome | GitHub |
|------|--------|
| Ryan dos Santos Veloso | [@Ryan](https://github.com/1s4ntos) |
| Guilherme Lombardi| [@Guilherme](https://github.com/Guilherme-Lombardi) |

---

## 🧠 Disciplinas Envolvidas

- Estrutura de Dados I

---

## 🏫 Informações Acadêmicas

- Universidade: **Universidade Braz Cubas**
- Curso: **Ciência da Computação**
- Semestre: 3º 
- Período: Manhã
- Professora orientadora: **Dra. Andréa Ono Sakai**
- Evento: **Mostra de Tecnologia 1º Semestre de 2025**
- Local: Laboratório 12
- Datas: 05 e 06 de junho de 2025

---

## 📄 Licença

MIT License — sinta-se à vontade para utilizar, estudar e adaptar este projeto.
