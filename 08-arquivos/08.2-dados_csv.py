import csv

dados_tabela = [
    ["Nome","Cargo","Idade"],
    ["Calos","Dev", 28]
    ["julia","Ausiliar", 19],
    ["Lucas", "Repositor", 23]
    ["gabriel", "ADM", 22]
]

with open("08.2-funcionarios.csv","w",encoding="utf-8",newline="") as arquivo_csv:
    escrever = csv.writer(arquivo_csv)
    escrever.writerow(dados_tabela)