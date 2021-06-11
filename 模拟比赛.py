import random
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示")
def getInputs():
    a=eval(input("请输入选手A的能力值（0-1）"))
    b=eval(input("请输入选手B的能力值（0-1）"))
    n=eval(input("模拟比赛的场次"))
    return a,b,n
def printSum(WinsA,WinsB):
    n=WinsA+WinsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(WinsA,WinsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(WinsB,WinsB/n))
def simonegame(proA,proB):
    scoreA,scoreB=0,0
    serving=random.choice(['A','B'])
    while scoreA!=15 and scoreB!=15:
        if serving=='A':
            if random.random()<proA:#random()会随机生成一个0到1的小数
                scoreA+=1
            else:
                serving='B'#能力不够则代表失败，交换发球
        else:
            if random.random()<proB:
                scoreB+=1
            else:
                serving='A'
    return scoreA,scoreB
def simNgames(n,proA,proB):
    WinsA,WinsB=0,0
    for i in range(n):
        scoreA,scoreB=simonegame(proA,proB)
        if scoreA>scoreB:
            WinsA+=1
        else:
            WinsB+=1
    return WinsA,WinsB

def main():
    printIntro()
    proA,proB,n=getInputs()
    WinsA,WinsB=simNgames(n,proA,proB)
    printSum(WinsA,WinsB)
main()
