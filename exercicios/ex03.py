# Desenvolva um programa que receba o raio (R) de uma circunferência,
# calcule e mostre a área desta circunferência.
# fórmula da área: A = PI * R2, sendo que PI vale 3,14.

# Exercício 03 - Q01
# Entrada de Dados
raio = float(input("Digite o raio da circunferencia: "))
pi = 3.14
area = pi * raio ** 2

# Saída de Dados
print("A áre da circunferência: %.2f" % area)


# Exercício 03 - Q02
# Desenvolva um programa que receba o salário de um funcionário,
# calcule e mostre seu novo salário com reajuste de 15%

# Entrada de Dados
salario = input("Digite o salário do funcionário: ")
salario = float(salario)
salario = salario * 1.15

# Saída de Dados
print("Novo salário: ", format(salario))
print("Novo salário: %.2f" % salario)


# Exercício 03 - Q03
# Desenvolva um programa que receba os valores do comprimento (C),
# da largura (L) e da altura (H)  de um paralelepípedo, calcule e mostre o volume desse paralelepípedo.
# Fórmula do volume de um  paralelepípedo: V = C . L . H

# Entrada de Dados
c = float(input("Entre com o comprimento do paralelepípedo: "))
l = float(input("Entre com a largura do paralelepípedo: "))
h = float(input("Entre com a altura do paralelepípedo: "))

# Processamento dos Dados
v = c * l * h

# Saída dos Dados
print("Volume do paralelepípedo: %.2f" % v)

# Exercício 03 - Q04
# Desenvolva um programa que receba o número de horas trabalhadas por um
# funcionário e quanto  esse funcionário recebe por hora trabalhada,
# calcule e mostre o valor que deve ser recebido por  esse funcionário.

# Entrada de Dados
ht = int(input("Digite as horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))

# Processamento dos Dados
salario = ht * valor_hora

# Saída dos Dados
print("O salário do funcionário é: %.2f" % salario)
