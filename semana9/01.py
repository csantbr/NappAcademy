def juros_simples(capital, taxa=0.1, n_periodos=2):
    if capital <= 0:
        raise Exception('Capital precisa ser maior que zero.')
    if taxa < 0 or taxa > 1:
        raise Exception('Taxa precisa estar entre 0 e 1.')
    if n_periodos <= 0:
        raise Exception('Período precisa ser maior que zero.')
    return capital + capital * taxa * n_periodos

if __name__ ==  "__main__":
    #print(f'Teste 1: {juros_simples(0, 1, 2)}')
    #print(f'Teste 2: {juros_simples(1, -1, 2)}')
    #print(f'Teste 3: {juros_simples(1, 1, -1)}')
    #print(f'Teste 4: {juros_simples(1, 1, 2)}')
    #print(f'Teste 5: {juros_simples("0", 1, 2)}')
    print(f'Teste 5: {juros_simples(0, -1, 2)}')
