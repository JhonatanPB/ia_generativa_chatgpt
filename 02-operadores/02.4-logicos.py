# 1. Operador AND (E) - Retorna True apenas se TODAS as condições forem verdadeiras
tem_sol = True
tem_dinheiro = True
vai_praia = tem_sol and tem_dinheiro

print("Vai a praia (AND): ", vai_praia)

#2. Operador OR (OU) - Retorna True se pelomenos uma condição for verdadeira
tem_carro = True
tem_bicicleta = True
pode_viajar = tem_sol and tem_dinheiro

print("Pode Viajar (OR): ", pode_viajar )

#3.Operador NOT (NÂO) - inverte o valor lógico
chovendo = False
fazer_caminhada = not chovendo 
print("Fazer Caminhada (NOT): ", fazer_caminhada)