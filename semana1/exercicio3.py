lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'Elen']
lista_nomes = lista_nomes + ['Mário', 'Arnaldo', 'Lucas', 'Maria Vitória']
lista_nomes = lista_nomes + ['Vitor', 'Ana Paula', 'Maria Aparecida']

# Seu código aqui
for item in lista_nomes:
    if len(item.split()) > 1:
        print(item)