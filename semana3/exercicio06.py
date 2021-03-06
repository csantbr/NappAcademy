import csv

def find_start_subtring_credit_card(lista, *paramether):
    list = []
    if paramether == None:
        return list
    else:
        for arg in paramether:
            for row in lista:
                if row[2].startswith(arg):
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
    print(find_start_subtring_credit_card(lista))
    print(find_start_subtring_credit_card(lista, '222', '223'))
    print(find_start_subtring_credit_card(lista, '222', '223', '224'))
    print(find_start_subtring_credit_card(lista, '5'))
