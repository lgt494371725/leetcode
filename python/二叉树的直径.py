class Solution(object):
    def __init__(self):
        self.ans=0
    def diameterOfBinaryTree(self, root):
        def depth(node):
            if not node:return 0
            L=depth(node.left)
            R=depth(node.right)
            self.ans=max(self.ans,L+R)
            return max(L,R)+1
        depth(root)
        return self.ans
