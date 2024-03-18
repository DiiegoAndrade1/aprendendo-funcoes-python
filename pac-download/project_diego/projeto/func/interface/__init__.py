from time import sleep
from projeto.func.numbers import *
from projeto.func.manipulacao_string import *

def operacao_calculator():
    while True: #loop infinto de somas
        print("""
        [ 0 ] SOMA
        [ 1 ] SUBTRAÇÃO
        [ 2 ] MULTIPLICAÇÃO
        [ 3 ] DIVISÃO
        """)
        escolha = int
        while True:
            try:
                escolha = int(input(f'Digite a sua escolha: '))
            except(ValueError, TypeError):
                print('\033[31mERRO: POR FAVOR, DIGITE UMA OPÇÃO VÁLIDA.\033[m')
                continue
            except KeyboardInterrupt:
                print('\033[31m\nERRO. O USUÁRIO DECIDIU NÃO DIGITAR ESSE NÚMERO.\033[m')
                return 0
            else:
                break
        linha()
        n1 = float
        n2 = float
        if escolha == 0:
            print('ESCOLHEU SOMA')
            while True:
                try:
                    n1 = float(input('Digite um numero pra somar: '))
                    n2 = float(input('Digite o segundo numero pra somar: '))
                except(ValueError, TypeError):
                    print('\033[31mERRO: POR FAVOR, DIGITE UM NUMERO INTEIRO VÁLIDO.\033[m')
                    continue
                except KeyboardInterrupt:
                    print('\033[31m\nERRO. O USUÁRIO DECIDIU NÃO DIGITAR ESSE NÚMERO.\033[m')
                    return 0
                else:
                    break
            print('SOMA')
            soma(n1, n2)
        elif escolha == 1:
            print('ESCOLHEU SUBTRAÇÃO')
            print('* Lembrando que se você tirar digitar o menor número primeiro o resultado será negativo!')
            n1 = float(input('Digite o numero primeiro número: '))
            n2 = float(input('Digite o outro numero menor: '))
            subt(n1, n2)
            #if n1 > n2:
                #subt(n1, n2)
            #else:
                #subt(n2, n1)
        elif escolha == 2:
            print('ESCOLHEU MULTIPLICAÇÃO')
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o outro número: '))
            mult(n1, n2)
        elif escolha == 3:
            print('ESCOLHEU DIVISÃO')
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número'))
            divi(n1, n2)
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Quer realizar mais alguma operação [S/N]: ')).strip().upper()[0]
        if resposta == 'N':
            sleep(1)
            print('SAINDO')
            sleep(1)
            print('DO')
            sleep(1)
            print('SISTEMA')
            sleep(1)
            print('gOOD bYE!')
            sleep(1)
            break
        linha()
