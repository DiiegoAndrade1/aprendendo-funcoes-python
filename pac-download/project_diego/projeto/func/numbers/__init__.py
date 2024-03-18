def mult(a, b): #O 'A E 'B' são dois PARÂMETROS
    resultado = a * b
    #print(f'{a:^} x {b:^} = {resultado}')
    print('{:.2f} x {:.2f} = {:.2f}'.format(a, b, resultado))


def subt(a, b):
    result = a - b
    #print(f'{a:^} - {b:^} = {result}')
    print('{:.2f} - {:.2f} = {:.2f}'.format(a, b, result))


def soma(a, b):
    result = a + b
    #print(f'{a:^} + {b:^} = {result}')
    print('{:.2f} + {:.2f} = {:.2f}'.format(a, b, result))

def divi(a, b):
    result = a / b
    print('{:.2f} ÷ {} = {}'.format(a, b, result))
