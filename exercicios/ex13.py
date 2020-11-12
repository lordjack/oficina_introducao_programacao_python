# Exercício 13 - Lista de Dados

# Exemplo 01
palestras = ['Django', 'Java', 'React', 'docker', 'PHP']  # lista declarada
print(palestras)
print(palestras[-5])  # imprimindo o objeto na posição -5 da lista.
palestras[0] = 'C#'  # alterando da posição zero ou -5 de Django para C#.

for i in range(0, len(palestras)):
    print('Palestras de :', palestras[i])

# Exemplo 02
a = list("Olá")
print(a)

print(len(a)) # len retorna o tamanho do vetor

print(a[0]) # define as posições que deseja retornar no vetor
print(a[1:3]) # define as posições que deseja retornar no vetor
print(a[:-1]) # define as posições que deseja retornar no vetor
print(a.reverse()) # retornar o vetor invertido