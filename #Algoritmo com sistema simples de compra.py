#Algoritmo com sistema simples de compra em loja

nome = input("Digite o nome do cliente: ")

valor_original = float(input("Digite o valor da compra: "))

valor_desconto = valor_original * 0.1 if valor_original > 100 or valor_original == 100 else 0

valor_final = valor_original - valor_desconto

print(f"cliente: {nome}; valor original: {valor_original}; valor final: {valor_final}")
