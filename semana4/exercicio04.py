from datetime import datetime

def copa(date):
    dateValue = datetime.today() - date
    return f'Se passaram {dateValue.days} dias desde a derrota do brasil na copa!'

if __name__ == "__main__":
    var = datetime(2014, 7, 8)
    print(copa(var))