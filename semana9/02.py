def soma_numeros(*args):
    soma = 0
    for item in args:
        try:
            soma = soma + item
        except TypeError:
            raise TypeError('Incompatibilidade de tipos. Verificar parâmetros')
    return soma

if __name__ == '__main__':
    #print(soma_numeros(2, 3, 5, 6))
    #print(soma_numeros(2, 'ok'))
    #print(soma_numeros(2, 3, [1, 2, 3]))
    #print(soma_numeros('2', '2'))
    #print(soma_numeros(5, 5.25))
