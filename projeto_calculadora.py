def soma(num_1, num_2):
    print(f'a soma de {num_1} por {num_2} é = a ', (num_1 + num_2))

def divisao(num_1, num_2):
    if num_2 != 0:
        print(f"A divisao de {num_1} por {num_2} é = {num_1 / num_2}")
    else:
        print("Não é possível dividir por zero.")


def multiplicacao(num_1, num_2):
    print(f'a multiplicacao de {num_1} por {num_2} é = a ', (num_1 * num_2))

def subtracao(num_1, num_2):
    print(f'a subtracao de {num_1} por {num_2} é = a ', (num_1 - num_2))

while True:
    try:
        numero_1 = int(input('Qual o primeiro numero: '))
        numero_2 = int(input('Qual o segundo numero: '))
        operacao = input('Qual a operacao voce quer fazer: (divisao, multiplicacao, subtracao e soma)')
        operacao = input("Qual operacao voce quer fazer: (divisao, multiplicacao, subtracao, soma) ou sair para encerrar: ")
        if operacao == "sair":
            break
        elif operacao == 'soma':
            soma(numero_1, numero_2)
        elif operacao == 'divisao':
            divisao(numero_1, numero_2)
        elif operacao == 'multiplicacao':
            multiplicacao(numero_1, numero_2)
        elif operacao == 'subtracao':
            subtracao(numero_1, numero_2)
        else:
            print('Operacao invalida')
    except ValueError:
        print('Entrada invalida. Por favor, insira apenas numeros.')
