import csv

def find_subtring_credit_card(lista, parametro='322'):
    list = []
    for row in lista:
        if parametro in row[2]:
            list.append(row[0])
    return list


def carregar_arquivo(path):
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            local_list.append(line)
    return local_list


if __name__ == "__main__":
    path = 'usernames.csv'
    lista = []
    lista = carregar_arquivo(path)
    print(find_subtring_credit_card(lista))
    print(find_subtring_credit_card(lista, '222'))
