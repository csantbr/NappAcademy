import csv

def find_subtring_credit_card(lista, parametro='322'):
    list = []
    for row in lista:
        if parametro in row["credit_card"]:
            list.append(row["name"])
    return list


def find_start_subtring_credit_card(lista, parametro='303'):
    list = []
    for row in lista:
        if row["credit_card"].startswith(parametro):
            list.append(row["name"])
    return list


def carregar_arquivo(path):
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            local_list.append(line)
    return local_list


if __name__ == "__main__":
    path = 'usernames.csv'
    lista = []
    lista = carregar_arquivo(path)
    print(find_subtring_credit_card(lista))
    print(find_subtring_credit_card(lista, '222'))
    print(find_start_subtring_credit_card(lista))
    print(find_start_subtring_credit_card(lista, '222'))

