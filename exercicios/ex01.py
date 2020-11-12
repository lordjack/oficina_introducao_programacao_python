# exercício 01

# entrada de dados
nome = "Jackson Meires"
idade = 33
altura = 1.74
peso = 78
endereco = "Rua ABCD"

# saida de dados, forma 01
print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura)
print("Peso: ", peso)
print("Endereço: ", endereco)

# saida de dados, forma 02 - Concatenando(juntar) as variaveis com a string(Caracter)
print("Nome: " + nome)
print("Idade: " + str(idade) + " Anos")
print("Altura: ",  str(altura))
print("Peso: ",  str(peso))
print("Endereço: ", endereco)

# saida de dados, forma 03
print("Nome: %s " % nome)
print("Idade: %d anos" % idade)
print("Altura: %.2f " % altura)
print("Peso: %.2f " % peso)
print("Endereço: %s" % endereco)
