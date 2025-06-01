# utils/tradutor.py

try:
    from deep_translator import GoogleTranslator
except ImportError:
    GoogleTranslator = None
    print("⚠️ Biblioteca deep_translator não instalada. Tradução será simulada.")

def traduzir_pt(texto: str) -> str:
    if GoogleTranslator:
        try:
            return GoogleTranslator(source='en', target='pt').translate(texto)
        except Exception as e:
            print(f"Erro na tradução: {e}")
            return texto
    else:
        # Tradução simulada
        return texto
