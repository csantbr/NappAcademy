lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'elen']
vogais = ['A', 'E', 'I', 'O', 'U']

# Seu código aqui
for item in lista_nomes:
    if item.upper().startswith(tuple(vogais)):
        print(item)