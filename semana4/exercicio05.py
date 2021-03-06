import csv
from datetime import date, datetime

def find_born_monday(lista):
    list = []
    for row in lista:
        if "birthdate" in row[-2]:
            continue
        date = datetime.strptime(row[-2], "%Y-%m-%d").date()
        if(date.weekday() == 0):
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
    nascidos_segunda_feira = find_born_monday(lista)
    for item in nascidos_segunda_feira:
        print(item)