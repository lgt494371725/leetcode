class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def traverse(root,val,pre=None,height=0):
            if root==None:
                return None
            if root.val==val:
                return root,pre,height
            if root.val<val:
                return traverse(root.right,val,root,height+1)
            else:
                return traverse(root.left,val,root,height+1)
        #注意这里！！递归往下的时候不要忘了每一层的递归结果都要return
        #如果只有if root.val==val的时候return 的话,只有找到val的函数会return
        #但由于他的上一层函数没有return无法接收结果，最后还是会返回None
        ploc,prenode1,height1=traverse(root,p.val)
        if traverse(ploc,q.val):
            return p
        qloc,prenode2,height2=traverse(root,q.val)
        if traverse(qloc,p.val):
            return q
        return prenode1 if height1<height2 else prenode2
#以上是错误答案，但有参考价值（少考虑了一种情况）

#方法一，最好的方法
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
#如果当前节点的值大于 pp 和 qq 的值，
#说明pp和qq应该在当前节点的左子树，因此将当前节点移动到它的左子节点
#如果当前节点的值小于 pp 和 qq 的值，
#说明pp和qq应该在当前节点的右子树，因此将当前节点移动到它的右子节点
#如果不满足上述两条，则说明当前节点就是分岔点
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor

#方法二，简述：记录到点p和到点q的所有路径，找最后一个相同点即是结果
















