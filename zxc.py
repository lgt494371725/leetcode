from Graph import Graph,Vertex
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
