# Exercício 08 - Estrutura Condicional Aninhada

# Construa um programa que receba como entrada a altura e o sexo de uma pessoa
# (letra ‘F’ para Feminino e letra ‘M’ para Masculino).
# Em seguida, calcule e escreva o peso ideal dessa pessoa, utilizando as  seguintes fórmulas:
# para homens: (72.7 * altura) – 58;
# para mulheres:(62.1 * altura) – 44.7;

# Entrada de Dados
altura = float(input("Entre com a altura da pessoa: "))
sexo = float(input("Entre com o sexo da pessoa: "))

# Processamento de Dados
if sexo == "M" or sexo == "m":
    peso_ideal = (72.7 * altura) - 58
    # Saída de Dados
    print("Peso ideal %.2f " % peso_ideal)
elif sexo == "F" or sexo == "f":
    print("Peso ideal %.2f " % peso_ideal)
else:
    print("Sexo inválido: %s" % sexo)
