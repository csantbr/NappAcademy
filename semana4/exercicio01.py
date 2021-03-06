from datetime import datetime

def lifeDays(date):
    dateValue = datetime.today() - date
    return f'Você possui {dateValue.days} dias de vida!'

if __name__ == "__main__":
    var = datetime(2001, 4, 3)
    print(lifeDays(var))