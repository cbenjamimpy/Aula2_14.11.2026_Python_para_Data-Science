# Exemplo 6 - Entrada de números decimais com vírgula

# Armazena o preço na variavel 'preco' e substitui a vírgula por ponto para conversão correta para float
preco = float(input("Digite o preço: ").replace(",", "."))
print(f"Preço: R$ {preco:.2f}")
