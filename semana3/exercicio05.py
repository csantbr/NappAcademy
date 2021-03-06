import csv

def find_born_in_month_and_gender(lista, paramether='03', gender='F'):
    list = []
    param = '-' + paramether + '-'
    for row in lista:
        if param in row[4] and gender in row[5]:
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
    print(find_born_in_month_and_gender(lista))
    print(find_born_in_month_and_gender(lista, '01'))
    print(find_born_in_month_and_gender(lista, '01', 'M'))
