class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adlist = {i:[] for i in range(numCourses)}
        for i in prerequisites:
            adlist[i[0]].append(i[1])
        visited = [0]*numCourses
        def dfs(Vertex):
            impossible = False#没有办法用nonlocal关键字，所以用这种做法
            visited[Vertex] = 1
            for i in adlist[Vertex]:
                if visited[i] == 0:
                    impossible=dfs(i)
                    if impossible:
                        break
                elif visited[i] == 1:
                    return True
            visited[Vertex] = 2
            return impossible 
        impossible = False
        for i in range(numCourses):
            if not impossible and visited[i] == 0:
                impossible = dfs(i)
        return not impossible

class Solution:
    def canFinish(self, numCourses, prerequisites):
        indev = [0]*numCourses
        adlist = {i:[] for i in range(numCourses)}
        visited = 0#无需用visited列表类型
        for i in prerequisites:
            adlist[i[0]].append(i[1])
            indev[i[1]]+=1
        queue = [i for i in range(numCourses) if indev[i]==0]
        while queue:
            current = queue.pop(0)
            visited += 1
            for i in adlist[current]:
                indev[i] -= 1
                if indev[i] == 0:
                    queue.append(i)
        return visited == numCourses
