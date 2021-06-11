#错误的做法，只有同属于1个分支的情况下该方法才适用
#如果2个树属于不同子树，就不行勒
class Solution(object):
    def findTarget(self, root, k):
        def recursion(root,k,time):
            if time==0 and k==0:
                return True
            if not root:
                return False
            a=recursion(root.left,k,time)
            b=recursion(root.right,k,time)
            c=recursion(root.left,k-root.val,time-1)
            d=recursion(root.right,k-root.val,time-1)
            return any([a,b,c,d])
        return recursion(root,k,2)
#方法1，遍历整棵树
class Solution(object):
    def findTarget(self, root, k):
        set1=set()
        def recursion(root,k,set1):
            if not root:
                return False
            if k-root.val in set1:
                return True
            set1.add(root.val)
            return recursion(root.left,k,set1) or recursion(root.right,k,set1)
        return recursion(root,k,set1)
#方法2同理，不过使用BFS迭代不是用递归,效率更高
class Solution(object):
    def findTarget(self, root, k):
        set1=set()
        queue=[root]
        while queue:
            current=queue.pop(0)
            if k-current.val in set1:
                return True
            set1.add(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False




    
