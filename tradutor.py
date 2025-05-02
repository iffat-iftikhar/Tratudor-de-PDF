import fitz  # PyMuPDF
from deep_translator import GoogleTranslator
from fpdf import FPDF

# Caminho do PDF original
pdf_path = "6bb30b.pdf"

# Nome do arquivo de saída
output_pdf_path = "manual_gsxr750_traduzido.pdf"

# Abrir o PDF original
doc = fitz.open(pdf_path)

# Tradutor automático
translator = GoogleTranslator(source='auto', target='pt')

# PDF de saída
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=10)

for page_num, page in enumerate(doc):
    text = page.get_text().strip()
    if text:
        try:
            translated = translator.translate(text)
            pdf.add_page()
            pdf.multi_cell(0, 5, f"Página {page_num + 1}\n\n{translated}")
            print(f"✅ Página {page_num + 1} traduzida.")
        except Exception as e:
            print(f"❌ Erro na página {page_num + 1}: {e}")

# Salvar arquivo traduzido
pdf.output(output_pdf_path)
print(f"\nTradução finalizada! Arquivo salvo como: {output_pdf_path}")
