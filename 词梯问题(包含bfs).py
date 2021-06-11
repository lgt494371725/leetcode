from Queue import Queue
from Graph import Vertex,Graph
def buildGraph(wordFile):
    d={}
    g=Graph()
    wfile=open(wordFile,'r')
    #建立水桶
    for line in wfile:
        word=line[:-1]#得到单词
        for i in range(len(word)):#如果是4字母单词，就4个桶
            bucket=word[:i]+'_'+word[i+1:]#第i个变成_
            if bucket in d:#有就说明属于同一个桶，加入
                d[bucket].append(word)
            else:#以bucket作为字典的key，value则是一个列表
                d[bucket]=[word]
    #同一个桶单词间建立边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1!=word2:
                    g.addEdge(word1,word2)
    return g
def bfs(g,start):#普通的bfs不需要清楚探索路径，但在该问题中需要路径
    #所以多了一些步骤
    start.setDistance(0)
    start.setPred(None)
    verQueue=Queue()
    verQueue.enqueue(start)
    while (verQueue.size()>0):
        currentV=verQueue.dequeue()
        for nbr in currentV.getConnections():
            if(nbr.getColor()=='white'):
                nbr.setColor('gray')
                nbr.setDistance(currentV.getDistance())
                nbr.setPred(currentV)
                verQueue.enqueue(nbr)
        currrentV.setColor('black')
def traverse(y):
    x=y
    while (x.getPred()):
        print(x.getid())
        x=x.getpred()
    print(x.getid())
wordgraph=buildGraph("字母文件名.txt")
bfs(wordgraph,wordgraph.getVertex('FOOL'))#以FOOL这个词为起始顶点
traverse(wordgraph.getVertex('SAGE'))#打印回溯到FOOL之间的路径
