def fibo_seq_start(val):
    fibo_list = [0, val]
    for c in range(0, 15):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    print(fibo_list)


def fibo_seq_terms(val):
    fibo_list = [0, 1]
    for c in range(0, val - 2):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    print(fibo_list)


def fibo_seq_till(val):
    fibo_list = [0, 1]
    while True:
        if fibo_list[-1] + fibo_list[-2] > val:
            break
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    print(fibo_list)


def ler_int(val):
    while True:
        try:
            return int(val)
        except:
            pass
        val = input('Digite um valor inteiro: ')


def menu():
    print('*'*5, 'SEQUENCIA DE FIBONACCI', '*'*5)
    print('(1) Inicia com valor N\n(2) N termos\n(3) N limita o valor máximo da sequência')
    escolha = ler_int(input('Escolha: '))
    while escolha not in range(1,4):
        escolha = ler_int(input('Digite um valor entre 1 e 3: '))
    return escolha
