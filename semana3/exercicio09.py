import csv

def carregar_arquivo(path):
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            local_list.append(line)
    return local_list

class CardNumber:
    def find_subtring_credit_card(self, lista, parametro):
        list = []
        for row in lista:
            if parametro in row["credit_card"]:
                list.append(row["name"])
        return list

    def find_start_subtring_credit_card(self, lista, parametro): 
        list = []
        for row in lista:
            if row["credit_card"].startswith(parametro):
                list.append(row["name"])
        return list


if __name__ == "__main__":
    lista = carregar_arquivo('usernames.csv')
    obj = CardNumber()
    print(obj.find_subtring_credit_card(lista, '222'))
    print(obj.find_start_subtring_credit_card(lista, '303'))