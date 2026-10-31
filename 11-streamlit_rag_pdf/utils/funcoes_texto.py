from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def ler_pdf(arquivos):
    text = ""
    for arquivo in arquivos:
        paginas_pdf = PdfReader(arquivo)
        for pagina in paginas_pdf.pages:
            conteudo = pagina.extract_text()
            if conteudo:
                text += conteudo + "\n"
    return text

def criar_texto_chunks(texto):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(texto)
    return chunks