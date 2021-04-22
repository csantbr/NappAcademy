def n_medias(*notas, **kwnotas):
    media = 0
    if notas:
        media = sum(notas)/float(len(notas))
    elif kwnotas:
        media = sum(kwnotas.values())/float(len(kwnotas))
    return media

if __name__ == '__main__':
    print(n_medias(1,2,3,4,5, valor1 = 1, valor2 = 2, valor3 = 3))