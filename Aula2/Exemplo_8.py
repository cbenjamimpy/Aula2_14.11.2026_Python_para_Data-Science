''' 
Exemplo 8 - Entrada de dados com tratamento de erros
'''
while True:
        try:

        # try: solicita ao usuário que digite sua idade e tenta converte-la para um número inteiro.
        # A função int() é usada para converter a entrada do usuário (que é uma sting) em um número inteiro.
    
            idade = int(input("Digite sua idade: "))
            print(f"Sua idade é {idade} anos.") # a função print () exibe a idade do usuário usando f-string para formatação da saída.
            if(idade<0):
                print('Digite uma idade valida')
            else:
                print(f"Sua idade é {idade} anos.")
            break

    # O bloco except é executado se ocorrer um erro durante a execução do bloco try.

        except ValueError:
    # O bloco except captura a exceção ValueError, que ocorre quando a conversão para inteiro
    # falha (por exemplo, se o usuário digitar uma string que não pode ser convertida para inteiro).
    # Nesse caso, uma mensagem de erro é exibida solicitando ao usuário que digite um número inteiro válido.
    
            print("Erro: digite um número inteiro válido.")
