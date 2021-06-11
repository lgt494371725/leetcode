class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(start,end):
            if start<=end:
                mid=(start+end)//2
                root=TreeNode(nums[mid])#无需把nums列表传入内部函数也可以直接访问
                root.left=helper(start,mid-1)
                root.right=helper(mid+1,end)
                return root
            return None
        return helper(0,len(nums)-1)
#二叉平衡树按中序遍历就是升序数组
