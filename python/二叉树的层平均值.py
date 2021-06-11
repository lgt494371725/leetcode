class Solution(object):
    def averageOfLevels(self, root):
        alist=[]
        queue=[root]
        while queue:
            value=0
            count=0
            for current in queue[:]:#注意这里的切片，循环内部append也不会对这里有影响
            #只会在下次循环应用，故实现了层序遍历
                value+=float(queue.pop(0).val)
                count+=1
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            alist.append(value/count)
        return alist
