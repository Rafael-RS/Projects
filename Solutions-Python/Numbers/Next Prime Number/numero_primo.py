def isprime(num):
    cont = 0
    for c in range(2, num):
        if num % c == 0:
            cont += 1
            break
    return False if cont != 0 else True


def prox_primo(num):
    if isprime(num):
        num += 1
    while not isprime(num):
        num += 1
    return num


x = 0
while True:
    print(f'Próximo primo: {prox_primo(x)}')
    x = prox_primo(x)
    if input('Deseja continuar (S/N)') in 'Nn':
        break
