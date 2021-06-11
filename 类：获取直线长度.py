import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
class Line:
    def __init__(self,p1,p2):
        self.x=p1.getx()-p2.getx()
        #直接p1.x-p2.x也是可以的
        self.y=p1.gety()-p2.gety()
        self.len=math.sqrt(self.x**2+self.y**2)

    def getlen(self):
        return self.len
p1=Point(1,1)
p2=Point(4,5)
line=Line(p1,p2)
print(line.getlen())
