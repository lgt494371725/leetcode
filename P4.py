counts=3
import random
answer=random.randint(1,10)
while counts>0:
    temp=input("猜数字")
    guess=int(temp)
    if guess==answer:
        print("正确")
        break
    else:
        if guess<answer:
            print("小了")
        else:
            print("大了")
    counts-=1
print("游戏结束")
