class Solution(object):
    def islandPerimeter(self, grid):
        def lengthcount(x,y):
            length=4
            if x>0 and grid[x-1][y]==1:
                length-=1
            if y>0 and grid[x][y-1]==1:
                length-=1
            if x<len(grid)-1 and grid[x+1][y]==1:
                length-=1
            if y<len(grid[0])-1 and grid[x][y+1]==1:
                length-=1
            return length
        result=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    result+=lengthcount(i,j)
        return result
#更简便的方法，在外面加一圈0包围原范围，然后仍从原来的地方开始遍历
#这样判断上下左右时就不会越界，不用进行条件判断
#length=[grid[i-1][j], grid[i+1][j], grid[i][j-1], grid[i][j+1]].count(0)
#可以把lengthcount函数简化成上面这样
