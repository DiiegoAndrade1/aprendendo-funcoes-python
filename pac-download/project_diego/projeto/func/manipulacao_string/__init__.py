def linha(tam=42):
    return '\033[35m=\033[m' * tam


def cabecalho(txt):
    print(f'\033[35m{linha()}\033[m')
    print(txt.center(42))
    print(f'\033[35m{linha()}\033[m')
