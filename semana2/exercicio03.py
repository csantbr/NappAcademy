from massa_dados import list_spend_money

def spend_by_subname(name):
    for register in list_spend_money:
        if name in register[0]:
            print(register)

def sum_by_subname(name):
    soma = 0.0
    for register in list_spend_money:
        if name in register[0]:
            if register[3] == '':
                soma += 0
            else:
                soma += float(register[3])
    return round(soma, 2)

if __name__ == "__main__":
    name = 'Brown'
    spend_by_subname(name)
    print('A soma total é: ')
    print(sum_by_subname(name))
