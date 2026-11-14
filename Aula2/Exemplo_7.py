# Exemplo 7 - Entrada de varios valores

nome, idade, cidade = input(
    "Digite nome, idade e cidade separados por espaço: "
).split() # Armazena os valores digitados pelo usuário nas variaveis 'nome', 'idade' e 'cidade'

idade = int(idade) # Converte a idade de string para inteiro

# Exibe o nome, idade e cidade do usuário usando f-string para formatação da sa´da.

print(f"{nome} tem {idade} anos e mora em {cidade}.")
