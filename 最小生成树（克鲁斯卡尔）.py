from Graph import Graph,Vertex
def MiniSpanTree_kruskal(g):
    result=0
    #首先构造边集数组并排序
    Edgelist=getedgelist(g)
    #使用并查集方法查看是否构成闭环
    #初始将所有顶点单独处于一个集合，每次加入一条边，判断开始点和终点是否处于一个集合
    #若是，则会构成闭环
    searchset={V.id:V.id for V in g}
    #这里用的是字典类型，如果顶点为数字则使用列表更方便
    choice=[]
    for edge in Edgelist:
        for i in searchset.keys():#循环遍历每个连通分支
            if edge[0] in searchset[i]:#判断在哪里连通分支内
                head=i
            if edge[1] in searchset[i]:
                tail=i
        if head!=tail:#不在一连通分支，则可用
            searchset[head]=searchset[head]+searchset[tail]#合并两个连通分支
            searchset[tail]=''#清空原连通分支（删除也行），因为被合并了
            choice.append(edge)
            result+=edge[-1]
    return choice,result
  
                

def getedgelist(g):
    alist=[]
    for V in g:
        for W in V.getConnections():
            alist.append([V.id,W.id,V.getweight(W)])
    alist.sort(key=lambda x:x[-1],reverse=False)
    return alist


  
cost,path={},{}           
g=Graph()
g.addEdge('a','c',3)
g.addEdge('a','b',1)
g.addEdge('c','b',2)
g.addEdge('c','d',4)
g.addEdge('c','e',4)
g.addEdge('d','e',2)
g.addEdge('d','f',3)
g.addEdge('b','d',5)
g.addEdge('e','f',5)
choice,result=MiniSpanTree_kruskal(g)

