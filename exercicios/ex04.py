# Exercício 04 - Estrutura Condicional

# Entrada de Dados
nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))

# Processameno de Dados
media = (nota1 + nota2)/2

if media >= 5:
   	# Saída de Dados
    print("Aprovado com média %.2f" % media)
else:
    print("Reprovado com média %.2f" % media)
