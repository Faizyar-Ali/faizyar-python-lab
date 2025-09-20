from datetime import datetime
class Birthday:
    def __init__(self,name,year,month,day):
        self.name=name
        self.year=year
        self.month=month
        self.day=day
    def calculate(self):
        today=datetime.now()
        age=today.year-(self.year+1)
        final_month=today.month+12-self.month
        final_day=today.day-self.day
        return f"🥳 you are now {age} years {final_month} month and {final_day} year old 🎉"
one=Birthday("Faizy",2006,12,3)
print(one.calculate())


            