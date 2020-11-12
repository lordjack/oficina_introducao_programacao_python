# Exercício 11 - Estrutura de repetição for

# Exemplo 01 - x vai de 0 a 2
x = 0
for x in range(3):
    print("O valor de x é: ", x)
print("Saiu do laço")

# Exemplo 02
for x in range(0, 3):
    print("O valor de x é: ", x)
print("Saiu do laço")

# Exemplo 03
for x in range(50, 100):  # x vai de 50 a 99
    if x == 88:
        break  # se x for igual a 88, sai do laço
    print(x)
print("Saiu do laço")

# Exemplo 04
total = 0
numero = int((input("Digite um número: ")))
if (numero % 2) == 0:
    numero = numero - 1

for i in range(numero, 0, -2):  # 3 parametro é o incremento ou decremento
    total = total + i
    print("Valor de i ", i)
print("A soma dos número impares é ", total)
