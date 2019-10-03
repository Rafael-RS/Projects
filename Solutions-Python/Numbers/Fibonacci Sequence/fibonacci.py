import funcoes
while True:
    escolha = funcoes.menu()
    if escolha == 1:
        funcoes.fibo_seq_start(funcoes.ler_int(input('Valor de inicio: ')))
    elif escolha == 2:
        funcoes.fibo_seq_terms(funcoes.ler_int(input('Quantos termos: ')))
    else:
        funcoes.fibo_seq_till(funcoes.ler_int(input('Máximo: ')))
    cont = input('Desesa continuar(S/N)?')
    if cont not in 'Ss':
        break
    print("\n" * 130)
print('FIM')
