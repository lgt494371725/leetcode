from Graph import Graph
def depth_first_search(graph,startV):#递归dfs
    order=[]
    visited={}
    def dfs(Vertex):
        visited[Vertex.id]=True
        order.append(Vertex.id)
        for V in Vertex.getConnections():
            if V.id not in visited:
                dfs(V)
    dfs(startV)
    for node in graph.verlist.values():#防止不联通的点未被访问
        if node.id not in visited:
            dfs(node)
    return order
def depth_first_search2(graph,startV):#非递归dfs，利用栈
    stack=[]#存储顶点实例
    order=[]#存储顶点id
    visited={}#{id：x}
    def dfs():
        while stack:#while else语句，如果被break了，则不会执行else
            node=stack[-1]
            for n in node.getConnections():
                if n.id not in visited:
                    order.append(n.id)
                    stack.append(n)
                    visited[n.id]=True
                    break#只推了与当前顶点相连的第一个点，然后break
            else:
                stack.pop()
'''每次推入与当前顶点相连的第一个点，来实现深度探索，并没有pop，如果单一点深度
到底，就会依次开始找其他相邻的点，如果都不行则会弹出栈，一直往前。直到遍历整颗树
'''
    stack.append(startV)
    order.append(startV.id)
    visited[startV.id]=True
    dfs()
    for node in graph.verlist.values():#同样，防止树不止一颗
        if node.id not in visited:
            stack.append(node)
            order.append(node.id)
            visited[node.id]=True
            dfs()
    return order
        
g=Graph()
startV=g.addVertex(1)
g.addEdge(1,2)
g.addEdge(2,5)
g.addEdge(1,5)
g.addEdge(2,3)
g.addEdge(2,4)
g.addVertex(0)
order=[]
order=depth_first_search2(g,startV) 
