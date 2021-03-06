lista_frases = ['Eu gosto de batatas', 'Eu estava andando de moto']
lista_frases += ['Ele estava comendo no restaurante']
lista_frases += ['O cachorro está passeando pelo parque']

# Seu código aqui
gerundio = ['ando', 'endo', 'indo']

for item in lista_frases:
    for palavra in item.split():    
        if (palavra).endswith(tuple(gerundio)):
            print(palavra)