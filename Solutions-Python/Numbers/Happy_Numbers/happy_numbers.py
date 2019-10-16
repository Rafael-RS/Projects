def ler_num(): #verifica se o input é numérico
    while True:
        n1 = input('Digite um número inteiro: ')
        if n1.isnumeric():
            return n1
        print('Valor invalido\n')


def separar(n1: str): #separa o valor lido em uma lista
    l1 = list()
    for c in n1:
        l1.append(c)
    return l1


def ishappy(l1: list):
    ciclos = 0
    while True:
        for pos, val in enumerate(l1):
            l1[pos] = int(val)
            l1[pos] = l1[pos] ** 2

        soma = sum(l1[:])

        if soma == 1:
            return True

        elif ciclos > 500:
            return False
        del l1
        l1 = separar(str(soma))
        ciclos += 1
        #print(f'ciclos = {ciclos}\n soma = {soma}\n lista = {l1}')


def main():
    print('NÚMEROS MÁGICOS!!')
    print('São números em que a soma do quadrado de cada digito é igual a 1')
    print('Exemplo de números felizes: 1, 7, 10, 13, 19, 23, 28, 31, 32, 44')
    z = ler_num()
    x = separar(z)
    if ishappy(x):
        print(f'O número {z} é feliz!')
    else:
        print(f'Depois de muitatas tentativas o numero {z} ficou triste por não conseguir atingir o numero 1')


main()
