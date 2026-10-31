def dividir_seguro(x,y):
    resultado = x / y
    return resultado

try:
 x = int(input("Digite um número:"))
 y = float(input("Digite outro número:"))

 valor_resultado = dividir_seguro(x,y)
 print(valor_resultado)

except ValueError:
    print("Apenas valores numéricos são permitidos")

except ZeroDivisionError:
    print("Divisões por zero não são possíveis")

else:
    print("Ovalor da divisão é",valor_resultado)    