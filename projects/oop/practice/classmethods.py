import datetime


class Employee:
    company_name = ''

    def __init__(self, name):
        self.company_name = name

    def change_company_name(self, new_name):
        self.company_name = new_name

    @staticmethod
    def is_working_day():
        day = datetime.date.today().weekday()
        if day < 5:
            return True
        else:
            return False
