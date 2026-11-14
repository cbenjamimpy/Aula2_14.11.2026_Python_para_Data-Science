# Exemplo 5 - Entrada de números decimais - float ()

nome_aluno = input("Digite o nome do aluno: ") # Armazena o nome do aluno na variavel 'nome'
idade_aluno = int(input("Digite a idade: ")) # Armazena a idade do aluno na variavel 'idade'
media_aluno = float(input("Digite a média: ")) # Armazena a média do aluno na variavel 'média'

print(f"Nome do aluno é {nome_aluno},"
f"ele tem {idade_aluno} anos"
f"e sua média é {media_aluno:.2f}."
)
