
def recMC(coinvaluelist,change,knownresult):
    mincoins=change
    if change in coinvaluelist:
        knownresult[change]=1#记录最优解
        return 1
    elif knownresult[change]>0:
        return knownresult[change]
    #查表成功，直接用最优解
    else:
        for i in [c for c in coinvaluelist if c<=change]:
            numcoins=1+recMC(coinvaluelist,change-i,knownresult)
            if numcoins<mincoins:
                mincoins=numcoins
                knownresult[change]=mincoins
                #将部分最优解记录在列表
    return mincoins

print(recMC([1,5,10,25],63,[0]*64))
