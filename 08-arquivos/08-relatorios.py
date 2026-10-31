# O modo w cria o arquivo "relatório.txt" na pasta raiz do projeto
with open("08-relatorio.txt","a", encoding="utf-8") as arquivo:
    arquivo.write("\nPrimeira linha:  atençãoa a primeir linha foi escrita\n")
    arquivo.write("Segunda linha: dimba")