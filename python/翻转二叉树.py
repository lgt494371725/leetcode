class Solution(object):
    def invertTree(self, root):
        if not root:return root
        left=self.invertTree(root.left)
        right=self.invertTree(root.right)
        root.left,root.right=right,left
        return root
#写的更麻烦点（无意义但可行）
class Solution(object):
    def invertTree(self, root):
        def tra(root):
            if not root:return 0
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left,root.right=root.right,root.left
        tra(root)
        return root
