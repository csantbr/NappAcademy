from massa_dados_situacao_teste import lista_pessoas

def extrair_novos_registros(list_old, list_new):
    lista = []
    for i in list_new:
        if i not in list_old:
            lista.append([i])
    return lista

if __name__ == "__main__":
    lista_antiga = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22)]
    lista_nova = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22), ('Pessoa 4', 23), ('Pessoa 5', 24)]
    lista_novos_registros = extrair_novos_registros(lista_antiga, lista_nova)
    print(lista_novos_registros)