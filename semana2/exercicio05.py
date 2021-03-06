from massa_dados_situacao_teste import lista_pessoas

def lista_simples(list):
    lista = []
    for i in list:
        if type(i[-1]) is tuple:
            lista.append((i[0], i[-1]))
    return lista

if __name__ == "__main__":
    # Teste 1
    pedaco = slice(0,2)
    entrada = lista_pessoas[pedaco]
    saida_esperada = [('daniellemosley', ('33.93113', '-117.54866')), ('rhodesrichard', ('39.00622', '-77.4286'))]
    saida = lista_simples(entrada)
    assert(saida == saida_esperada)

    # Teste 2
    entrada = []
    saida_esperada = []
    saida = lista_simples(entrada)
    assert(saida == saida_esperada)

    # Teste 3
    entrada = 'string'
    saida_esperada = []
    saida = lista_simples(entrada)
    assert(saida == saida_esperada)