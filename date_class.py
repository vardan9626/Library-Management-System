class Date:
    def __init__(self,day,month,year):
        self.__d = day
        self.__m = month
        self.__y = year
        self.correct_date_flag = self.correct_date(self)==1

    @property
    def day(self): return self.__d
    @property
    def month(self): return self.__m
    @property
    def year(self): return self.__y
    @property
    def date(self):
        if not self.correct_date_flag:
            self = self.add_days(0)
        return f"{self.__d}/{self.__m}/{self.__y}"
    
    def correct_date(self, date):
        d = date.day
        m = date.month
        y = date.year
        months_with_31_days = [1,3,5,7,8,10,12]
        months_with_30_days = [4,6,9,11]
        if m > 12: return 0
        if m in months_with_30_days and d>30: return -1
        if m in months_with_31_days and d>31: return -2
        if m == 2 and d > self.days_in_feb(y): return -3
        return 1
    @staticmethod
    def days_in_feb(year):
            return 28 if year%4 else 29
    
    @staticmethod
    def diff(date1, date2):
        pass
    
    def add_days(self,days):
        d = self.__d + days
        m = self.__m
        y = self.__y
        tmp = Date(d,m,y)
        while self.correct_date(tmp) != 1:
            
            val = self.correct_date(tmp)
            print(f"The error code is: {val}")
            if val == 0:
                m-=12
                y+=1
            elif val == -1:
                m+=1
                d-=30
            elif val == -2:
                m+=1
                d-=31
            else:
                m+=1
                d-=self.days_in_feb(y)
            tmp = Date(d,m,y)
        ans = Date(d,m,y)
        return ans
    
    