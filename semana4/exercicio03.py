from datetime import datetime

def ageYears(date):
    dateToday = datetime.today()
    if(date >= dateToday):
        years = dateToday.year - date.year
        return f'Você nasceu em {date.year} e tem {years} anos de idade'
    else:
        years = dateToday.year - date.year
        years -= 1
        return f'Você nasceu em {date.year} e tem {years} anos de idade'

if __name__ == "__main__":
    var = datetime(2001, 4, 3)
    print(ageYears(var))