class Solution(object):
    def __init__(self):
        self.list1=[]
    def preorder(self, root):
        if not root:return
        self.list1.append(root.val)
        for i in root.children:
            self.preorder(i)
        return self.list1
