from Graph import Graph,Vertex
#由于导入的图用的是邻接表形式，所以这里直接设置邻接矩阵
def floyd(g):
    #初始化两个矩阵
    length=len(g.getVers())#顶点数目
    matrix=[[0 for col in range(length)] for row in range(length)]#记录顶点i到顶点j的距离，初始化为邻接矩阵
    F=999#表示无法到达
    matrix[0] = [0, 5, 7, F, F, F, 2]
    matrix[1] = [5, 0, F, 9, F, F, 3]
    matrix[2] = [7, F, 0, F, 8, F, F]
    matrix[3] = [F, 9, F, 0, F, 4, F]
    matrix[4] = [F, F, 8, F, 0, 5, 4]
    matrix[5] = [F, F, F, 4, 5, 0, 6]
    matrix[6] = [2, 3, F, F, 4, 6, 0]#显然是对称矩阵，所以是无向图
    P=[[0 for col in range(length)] for row in range(length)]#记录前驱顶点
    for v in range(length):
        for w in range(length):
            P[v][w]=w#需要初始化，如0到1必须经过1
    for k in range(length):
        for v in range(length):
            for w in range(length):
                if matrix[v][w]>matrix[v][k]+matrix[k][w]:
                    matrix[v][w]=matrix[v][k]+matrix[k][w]
                    P[v][w]=P[v][k]

https://www.jianshu.com/p/f73c7a6f5a53
