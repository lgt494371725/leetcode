def genLegalMoves(x,y,bdsize):#当前坐标以及棋盘大小
    newMoves=[]#储存所有合法的可移动位置
    moveoffsets=[(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),
                 (1,2),(2,-1),(2,1)]#马走日的八种可能情况
    for i in moveoffsets:
        newx=x+i[0]
        newy=y+i[1]
        if legalcoord(newx,bdsize) and legalcoord(newy,bdsize):
            newMoves.append((newx,newy))
    return newMoves
def legalcoord(x,bdsize):#检查移动是否超出棋盘
    if x>=0 and x<=bdsize:
        return True
    else:
        return False
def knightGraph(bdsize):#建立合法走棋图
    ktGraph=Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeid=posToNodeid(row,col,bdsize)#给每个格子都编号，自定义
            newpos=genLegalMoves(row,col,bdsize)#该格子的下一步合法移动
            for e in newpos:#将该格子和所有合法移动的格子连接边
                nid=posToNodeid(e[0],e[1],bdsize)
                ktGraph.addEdge(nodeid,nid)
    return ktGraph
def posToNodeid(row,col,bdsize):
    return row*bdsize+col
def knightTour(n,path,u,limit):#n当前路径长度，path列表类型表示路径，可以理解为栈
    u.setColor('gray')#u当前顶点,limit搜索总深度
    path.append(u)#当前顶点加入路径
    if n<limit:
        nbrlist=list(u.getConnections())#当前顶点所有的合法移动，优化算法：orderByAvail(u)
        i=0
        done=False
        while i <len(nbrlist) and not done:
            if nbrlist[i].getColor()=='white':#白色说明还未经过
                done=knight(n+1,path,nbrlist[i],limit)#路径长度加1
            i+=1
        if not done:#如果无法完成总深度，则尝试回溯
            path.pop()
            u.setColor('white')
    else:
        done=True
    return done
#该方法只会找到一种解决方案后就停止，复杂度为O（k的n次方）n为棋盘格数目，是指数级别的算法，性能很差
#改进方法如下，配合笔记第70页
def orderByAvail(n):#n为当前顶点
    reslist=[]
    for v in n.getConnections():#所有与n相连的顶点中，为白色的即未探索的才需要考虑加入列表
        if v.getColor()=='white':
            c=0
            for w in v.getConnections():#计算与这个顶点相连的可探索顶点有多少个
                if w.getColor()=='white':
                    c+=1
            reslist.append((c,v))
    reslist.sort(key=lambda x :x[0])#以列表中每个元素（每个元素都是一个元组）的第一个元素（即c）的大小为根据进行排列
    return [y[1] for y in reslist]#返回以排序后的顶点组成的列表
