import random as r

class Turtle:
    def __init__(self):
        self.power=100
        #初始位置随机
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)

    def move(self):
        new_x=self.x+r.choice([1,2,-1,-2])
        new_y=self.y+r.choice([1,2,-1,-2])
        #检查是否超出边界
        if new_x<0:
            self.x=-new_x
        elif new_x>10:
            self.x=10-(new_x-10)
        else:
            self.x=new_x
        if new_y<0:
            self.y=-new_y
        elif new_y>10:
            self.y=10-(new_y-10)
        else:
            self.y=new_y

        self.power-=1
        return (self.x,self.y)
    def eat(self):
        self.power+=20
        if self.power>100:
            self.power=100
class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
        
    def move(self):
        new_x=self.x+r.choice([1,-1])
        new_y=self.y+r.choice([1,-1])
        #检查是否超出边界
        if new_x<0:
            self.x=-new_x
        elif new_x>10:
            self.x=10-(new_x-10)
        else:
            self.x=new_x
        if new_y<0:
            self.y=-new_y
        elif new_y>10:
            self.y=10-(new_y-10)
        else:
            self.y=new_y

        return (self.x,self.y)

turtle=Turtle()
fish=[]
for i in range(10):
    new_fish=Fish()
    fish.append(new_fish)
while True:
    if not len(fish):
        print("鱼儿都吃完了，游戏结束")
        break
    if not turtle.power:
        print("乌龟体力耗尽，游戏结束")
        break
    pos=turtle.move()
     # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
    # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了
    for each_fish in fish[:]:
        if each_fish.move()==pos:
            #鱼被吃掉了
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼被吃掉了")















    
