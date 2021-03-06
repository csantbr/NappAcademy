from massa_dados import list_spend_money

def spend_by_gender(gender):
    for register in list_spend_money:
        if gender.upper() == register[2]:
            print(register)

def sum_by_gender(gender):
    soma = 0.0
    for register in list_spend_money:
        if gender.upper() == register[2]:
            if register[3] == '':
                soma += 0
            else:
                soma += float(register[3])
    return round(soma, 2)

if __name__ == "__main__":
    gender = 'M'
    spend_by_gender(gender)
    print('A soma total é: ')
    print(sum_by_gender(gender))
