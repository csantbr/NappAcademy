from datetime import date, datetime


# noinspection PyBroadException
class MyCalendar:
    def __init__(self, *args):
        self.datas = []
        self.datas = self.add_holiday(*args)

    def add_holiday(self, *args):
        for param in args:
            if isinstance(param, date):
                self.datas.append(param)
            elif type(param) is str:
                try:
                    data = datetime.strptime(param, '%d/%m/%Y').date()
                    self.datas.append(data)
                except Exception:
                    pass
            self.datas = list(set(self.datas))
        return self.datas

    def check_holiday(self, data):
        if isinstance(data, date):
            return data in self.datas
        elif type(data) is str:
            try:
                data = datetime.strptime(data, '%d/%m/%Y').date()
                return data in self.datas
            except Exception:
                return False
