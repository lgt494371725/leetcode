class LeapYear:
    def __init__(self,thisyear):
        self.thisyear=thisyear
    def isLearYear(self,year):
        if (year%4==0 and year%100!=0)or (year%400==0):
            return True
        else:
            return False
    def __iter__(self):
        return self
    def __next__(self):
        while not self.isLearYear(self.thisyear):
            self.thisyear-=1
        temp=self.thisyear
        self.thisyear-=1
    #不这么做的话下次迭代无法进行，因为直接被闰年卡住了
        return temp

print("设定时请输入今年年份")
leapyear=LeapYear(2019)
for i in leapyear:
    if i >=2000:
        print(i)
    else:
        break
