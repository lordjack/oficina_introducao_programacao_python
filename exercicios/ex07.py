# Exercício 07 - Estrutura Condicional Aninhada

# Entrada de Dados
sb = float(input("Entre com o salário base: "))

# Processamento de Dados
if sb >= 1000 and sb <= 2500:
    ir = sb * 0.10
elif sb > 2500:
    ir = sb * 0.15
else:
    ir = 0
# Saída de Dados
    print("Imposto de renda a pagar: %.2f " % ir)
