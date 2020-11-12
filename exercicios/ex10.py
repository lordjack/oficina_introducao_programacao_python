# Exercício 10 - Estrutura de repetição While
# Desenvolva um programa que recebe números inteiros digitados pelo  usuário e calcula
# a soma entre esses números e a média. Só parar de  digitar os números quando
# o usuário digitar zero. Utilizar while.
# Inicialização das variáveis dados
numero = 5
cont = 0
soma = 0

# condicional do laço
while numero != 0:
    # entrada de dados
    numero = int(input("Digite um número: "))
    # condicional 
    if numero != 0:
        # processamento de dados
        soma = soma + numero
        cont = cont + 1
# saiu do laço
media = soma / cont

# saída de dados
print("A soma é igual a %d e a média é igual a %.2f" % (soma, media))
