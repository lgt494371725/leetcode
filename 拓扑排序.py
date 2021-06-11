from Graph import Graph,Vertex
from Queue import Queue
def topologicalSort(g):  
    #创建入度字典
    indic=dict((V.id,0)for V in g)
    #或者用字典推导式indic={V.id:0 for V in g}
    for V in g:
        for w in V.getConnections():
            indic[w.id]+=1
    #开始进行排序，利用队列结构
    order=[]#存储访问顺序
    q=Queue()
    for name in indic:
        if indic[name]==0:
            order.append(name)
            q.enqueue(name)
    while q.size():
        nameid=q.dequeue()
        V=g.getvertex(nameid)
        for w in V.getConnections():
            indic[w.id]-=1
            if indic[w.id]==0:
                q.enqueue(w.id)
                order.append(w.id)
    return order
g=Graph()
g.addEdge('a','f')
g.addEdge('a','b')
g.addEdge('b','c')
g.addEdge('b','d')
g.addEdge('b','f')
g.addEdge('c','d')
g.addEdge('d','e')
g.addEdge('d','f')
g.addEdge('e','f')
print(topologicalSort(g))
