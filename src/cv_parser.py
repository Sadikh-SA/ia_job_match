import fitz  # PyMuPDF pour extraire le texte des PDF

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text() for page in doc])
        return text
    except Exception as e:
        print("❌ Erreur lors de l'extraction du texte :", e)
        return ""

# Test avec un fichier exemple
if __name__ == "__main__":
    pdf_path = "data/mon_cv.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    print("🔹 Texte extrait du CV :\n", extracted_text[:500])  # Affiche les 500 premiers caractères
