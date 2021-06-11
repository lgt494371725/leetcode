#注意，是左叶子之和！不是左节点
class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root: return 0
        result=0
        stack1=[root]
        while stack1:
            current=stack1.pop()
            lnode=current.left
            rnode=current.right
            if lnode:
                if not lnode.left and not lnode.right:
                    result+=lnode.val
                else:
                    stack1.append(lnode)
            if rnode:
                stack1.append(rnode)
        return result
