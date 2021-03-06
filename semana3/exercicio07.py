import csv
import json

def carregar_dicionario_websites(path):
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            local_list.append(line)
    
    dictionary = {}
    for key in local_list:
        if key["name"]:
            chave = {key["name"]: key["website"]}
            dictionary.update(chave)
    return dictionary


if __name__ == "__main__":
    path = 'names.csv'
    dicionario = {}
    dicionario = carregar_dicionario_websites(path)
    json_object = json.dumps(dicionario, indent=4)
    print(json_object)
