def dpMakeChange(coinvaluelist,change,mincoins,coinused):
    #coinvaluelist--币种,change--零钱数目，mincoins--记录最少硬币个数的列表,coinused--用于追踪用了哪些硬币凑成最小方案
    #从1分钱开始计算最少银币个数
    for cents in range(1,change+1):
        coinCount=cents #设一个最大值
        newcoin=1 #记录使用硬币的路径,默认使用最小的1
        #减去每个币种，向后查最少硬币数
        for j in [c for c in coinvaluelist if c<=cents]:
            if mincoins[cents-j]+1<coinCount:
                coinCount=mincoins[cents-j]+1
                newcoin=j
                #记录此时最少数目用的硬币
        mincoins[cents]=coinCount
        coinused[cents]=newcoin
    return mincoins[change]
def printcoin(coinused,change):
    coin=change
    while coin>0:
        thiscoin=coinused[coin]
        print(thiscoin)
        coin=coin-thiscoin
amnt=63
clist=[1,5,10,21,25]
coinused=[0]*(amnt+1)

coinCount=[0]*(amnt+1)
print(dpMakeChange(clist,amnt,coinCount,coinused))
 
