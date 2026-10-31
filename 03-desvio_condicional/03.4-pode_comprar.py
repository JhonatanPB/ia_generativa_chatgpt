# Exemplo de encadeiamento / aninhamento
tem_cartão = True
saldo =  200.0

if tem_cartão:
   if saldo >= 100:
      print("Compra aprovada, Saldo suficiente")
   else:
      print("Compra negada, saldo insuficiente")

else:
   print("Erro, cartão não inserido")