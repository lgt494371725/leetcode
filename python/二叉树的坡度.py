#错误答案
class Solution(object):
    def __init__(self):
        self.list1=[]
    def findTilt(self, root):
        def traversal(root):
            if not root:return 0
            L=traversal(root.left)
            R=traversal(root.right)
            self.list1.append(abs(L-R))
            return root.val+traversal(root.left)+traversal(root.right)
#只有上面这一行不同，导致了错误，因为总共递归了两次，所以列表多append了一次，导致了误差
        traversal(root)
        return sum(self.list1)
#正确答案
class Solution(object):
    def __init__(self):
        self.list1=0
    def findTilt(self, root):
        def traversal(root):
            if not root:return 0
            L=traversal(root.left)
            R=traversal(root.right)
            self.list1+=abs(L-R)
            return root.val+L+R
        traversal(root)
        return self.list1
