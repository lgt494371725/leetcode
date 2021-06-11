#第一种，使用中序遍历，同时用列表保存遍历的结果
class Solution(object):
    def getMinimumDifference(self, root):
        alist=[]
        def midordertraversal(root):
            if root==None:return
            midordertraversal(root.left)
            alist.append(root.val)
            midordertraversal(root.right)
        midordertraversal(root)
        return min(alist[i]-alist[i-1] for i in range(1,len(alist)))
#第二种同样使用中序遍历，但遍历时记录前驱节点，同时更新最小差
class Solution(object):
    def getMinimumDifference(self, root):
        global ans,pre
        ans=2**31-1
        pre=-1
        def midorder(root):
            global ans,pre
            if root==None:return
            midorder(root.left)
            if pre==-1: pre=root.val
            else:
                ans=min(ans,root.val-pre)
                pre=root.val
            midorder(root.right)
        midorder(root)
        return ans
