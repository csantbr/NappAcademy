def juros_compostos(valor_inicial, juros, tempo):
    if(type(valor_inicial) is str or type(juros) is str or type(tempo) is str):
        raise TypeError("Os parametrôs só podem ser números!")
    juros = juros/100
    valor_final = valor_inicial * (1+juros)**tempo
    return round(valor_final, 2)
