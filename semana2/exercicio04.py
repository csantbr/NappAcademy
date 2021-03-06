from massa_dados import list_spend_money

def spend_by_login(login, limit=1000):
    for register in list_spend_money:
        if login == register[1] and register[3] == '':
            pass
        elif login == register[1] and float(register[3]) <= limit:
            print(register)
        else:
            pass

def sum_by_login(login, limit=1000):
    soma = 0.0
    for register in list_spend_money:
        if login == register[1] and register[3] == '':
            pass
        elif login == register[1] and float(register[3]) <= limit:
            soma += float(register[3])
        else:
            pass
    return round(soma, 2)

if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login, 1200)
    print('A soma total até 600: ')
    print(sum_by_login(login))
    print('A soma total até 1200: ')
    print(sum_by_login(login, 1200))