class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root: return False
        if not root.left and not root.right:return targetSum-root.val==0
        else:
            return self.hasPathSum(root.left,targetSum-root.val) or \
            self.hasPathSum(root.right,targetSum-root.val) 
#记住一定要到叶节点，所以要判断有没有左右子树
