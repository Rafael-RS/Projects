import funções
while True:
    escolha = funções.menu()
    if escolha == 1:
        funções.fibo_seq_start(funções.ler_int(input('Valor de inicio: ')))
    elif escolha == 2:
        funções.fibo_seq_terms(funções.ler_int(input('Quantos termos: ')))
    else:
        funções.fibo_seq_till(funções.ler_int(input('Máximo: ')))
    cont = input('Desesa continuar(S/N)?')
    if cont not in 'Ss':
        break
    print("\n" * 130)
print('FIM')
