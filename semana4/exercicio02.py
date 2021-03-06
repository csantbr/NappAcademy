from datetime import datetime, timedelta

def addWeek():
    dateValue = datetime.today() + timedelta(days=17)
    return f'o dia será {dateValue.day} do mês {dateValue.month} de {dateValue.year}'

if __name__ == "__main__":
    print(addWeek())