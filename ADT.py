class date:
    def __init__(self,a,b,c):
        self.d=a
        self.m=b
        self.y=c
    def day(self):
        print("day=",self.d)
    def month(self):
        print("month=",self.m)
    def year(self):
        print("year=",self.y)
    def monthName(self):
        months=["unknown","january","febraury","march","april","may","june","july","august","sepatember","october","november","december"]
        print("monthName:",months[self.m])
    def isLeapYear(self):
       if(self.y%4==0)and(self.y%100!=0):
        print("it is a Leapyear")
       else:
        print("it is not a leapyear")
d1=date(3,8,2024)
d1.day()
d1.month()
d1.year()
d1.monthName()
d1.isLeapYear()