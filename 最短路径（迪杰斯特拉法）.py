from Graph import Graph,Vertex

def dijkstra(g,startV):
    cost={}#保存起点到其余顶点的最短距离
    cost=startV.connectedTo.copy()#注意不能把一个字典复制给另一个字典，不然修改的话会同时修改，要通过复制
    for V in g:
        if V not in startV.connectedTo:
            cost[V]=999
    cost[startV]=0
    #初始化起点开始时到各点的距离，999则表示之间没有边，到自身距离为0
    parents={V.id:startV.id for V in g}#储存每个点对应的前驱节点,初始化都为起点
    visited=[startV]#储存已经访问过的节点
    for i in range(len(cost)-1):#重复n-1次循环，每次找到一个长度的最短路径
        minimal=999
        for k in cost:#找到当前长度的最小值节点
            if k not in visited and cost[k]<minimal:
                minimal=cost[k]
                currentV=k
        visited.append(currentV)
        for V in g:#以该节点为中介，更新最短路径
            if V not in visited and ((minimal+currentV.connectedTo.get(V,999))<cost[V]):#这里注意一定要用字典的get方法，不然会出现KeyError
                cost[V]=minimal+currentV.getweight(V)
                parents[V.id]=currentV.id#设置前驱节点
    return cost,parents
cost,path={},{}
g=Graph()
g.addEdge('a','c',3)
g.addEdge('a','b',6)
g.addEdge('c','b',2)
g.addEdge('c','d',3)
g.addEdge('c','e',4)
g.addEdge('d','e',2)
g.addEdge('d','f',3)
g.addEdge('b','d',5)
g.addEdge('e','f',5)
startV=g.getvertex('a')
cost,path=dijkstra(g,startV)
for V in cost:
    print(V.id,cost[V])

