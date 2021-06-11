class Solution(object):
    def mergeTrees(self, root1, root2):
        if not root1 and not root2:return
        newNode=TreeNode()
        if root1 and root2:
            newNode.val=root1.val+root2.val
            newNode.left=self.mergeTrees(root1.left,root2.left)
            newNode.right=self.mergeTrees(root1.right,root2.right)
        elif root1:
            newNode.val=root1.val
            newNode.left=root1.left
            newNode.right=root1.right
        else:
            newNode.val=root2.val
            newNode.left=root2.left
            newNode.right=root2.right
        return newNode
