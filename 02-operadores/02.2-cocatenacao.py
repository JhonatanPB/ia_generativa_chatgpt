#1.Concatenação simples de variáveis textos
nome = "Maria"
sobrenome = "da Silva"
nome_completo = nome + " " + sobrenome

print("Nome completo: ", nome_completo )

#2.Concatenação combinando texto com números
idade = 32
mensagem = "Olá, meu nome é " + nome_completo + " e eu tenho " + str(idade) + " anos "

print(mensagem)

#3.Números inceridos pelo usuário
nota_1 = float(input("Digiti a primeira nota:"))
nota_2 = float(input("Digiti a segunda nota:"))
nota_3 = float(input("Digiti a terceira nota:"))

media = (nota_1+nota_2) / 3

print("A media das notas é: ", media)
print(f"A media das notas é: {round(media):.2f}")