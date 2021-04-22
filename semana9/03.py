import json


def criar_json(**kwargs):
    return json.dumps(kwargs)

if __name__ == '__main__':
    #print(criar_json(nome = "vagner", nome = "vagnao", time = "PDI", tempo_napp = "6 meses"))
    print(criar_json(2 = "caio", time = "PDI", tempo_napp = "2 meses"))
    print(criar_json(nome = "caio", time = "PDI", tempo_napp = "2 meses"))
    print(criar_json(nome = "evandro", time = "PDI", tempo_napp = "3 anos e 8 meses", funcao = "capitao"))