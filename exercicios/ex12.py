# Exercício 12 - Estrutura de repetição for

# Questão 01
# Desenvolva um programa que calcule e o quadrado dos números inteiros
# compreendidos entre 10 e 150. Utilizar for.

for i in range(50, 100, 5):
    print("%d ao quadrado = %d" % (i, i*i))

# Questão 02
# Desenvolva um programa que receba um número inteiro, calcule e
# mostre o seu fatorial. (Exemplo de Fatorial: se o número 4 for digitado,
# o programa deverá fazer 1*2*3*4 e mostrar como resultado 24,
# se o número digitado for 5 o programa deverá fazer 1*2*3*4*5
# e mostrar como resultado 120). Utilizar for.

numero = int(input("Digite um número: "))
result = 1
for i in range(1, numero+1):
    result = result * i
print("Fatorial de ", numero, result)

numero = int(input("Digite um número: "))
result = 1
# indo de numero até , decrementando em 1
for i in range(numero, 0, 1):
    result = result * i
print("Fatorial de ", numero, result)

# Questão 03
# Desenvolva um programa que recebe um número inteiro e mostra a  tabuada desse número.
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print("%d x %d = %d" % (numero, i, numero*i))

# Questão 04
# Desenvolva um programa que receba um número inteiro, verifique e  mostre se esse número é primo ou não.
numero = int(input("Digite um número: "))
cont = 0
for i in range(2, numero):
    if numero % i == 0:
        cont = cont + 1
        break
if cont == 0:
    print("%d é primo " % numero)
else:
    print("%d não é primo " % numero)
