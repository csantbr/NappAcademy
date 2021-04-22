lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio']
lista_meses += ['junho', 'julho', 'agosto', 'setembro']
lista_meses += ['outubro', 'novembro', 'dezembro']

meses = dict(zip(
    list(range(1, 13)),
    lista_meses))


def data_por_extenso(data):
    data = data.split('/')
    try:
        return data[0] + ' de ' + meses[int(data[1])] + ' de ' + data[2]
    except KeyError:
        raise KeyError('Mês inválido')

if __name__ == '__main__':
    #print(data_por_extenso("03/04/2021"))
    #print(data_por_extenso(03/04/2021))
    print(data_por_extenso("03/13/2021"))
