from massa_dados import list_spend_money

def spend_by_login(login):
    for register in list_spend_money:
        if login == register[1]:
            print(register)

def sum_by_login(login):
    soma = 0.0
    for register in list_spend_money:
        if login == register[1]:
            if register[3] == '':
                soma += 0
            else:
                soma += float(register[3])
    return round(soma, 2)
            
if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login)
    print('A soma total é: ')
    print(sum_by_login(login))
