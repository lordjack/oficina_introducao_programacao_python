# Exercício 05 - Estrutura Condicional

# Entrada de Dados
sb = float(input("Entre com o salário base: "))

# Processamento de Dados
if sb >= 1000 and sb <= 2500:
    ir = sb * 0.10
# Saída de Dados
    print("Imposto de renda a pagar: %.2f " % ir)
