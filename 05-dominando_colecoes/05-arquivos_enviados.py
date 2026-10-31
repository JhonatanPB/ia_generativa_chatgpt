#Lista de arquis encontrados no diretório
arquivos_enviados = ["manual.pdf", "foto.png", "contrato.PDF","virus.exe","relatorio.pdf","anotacoes.txt"]

# Lista de arquivos pdf (vazias)
pdfs_validos = []

for arquivo in arquivos_enviados:                    
    if arquivo.lower().endswith(".pdf"):  #endswith para verificar o final do arquivo
        pdfs_validos.append(arquivo)

print("Lista completa", arquivos_enviados)
print("Arquivos de PDF", pdfs_validos)