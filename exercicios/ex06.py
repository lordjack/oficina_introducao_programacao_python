# Exercício 06 Q01 - Estrutura Condicional

# Faça um programa para ler dois números inteiros e mostre-os em ordem crescente
# Entrada de Dados
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# Processamento de Dados
if n1 < n2:
    # Saída de Dados
    print("%d e %d " % (n1, n2))
if n2 < n1:
    print("%d e %d " % (n2, n1))
else:
    print("São iguais: %d " % n1)

# Exercício 06 Q02 - Estrutura Condicional
n1 = int(input("Digite um número: "))
if n1 % 2 == 0:
    print("%d é par" % n1)
else:
    print("%d é ímpar" % n1)
