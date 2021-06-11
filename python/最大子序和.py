class Solution(object):
    def maxSubArray(self, nums):#第一种，运行太慢
        if nums==[]: return 0
        length=1
        maxv=max(nums)
        while length!=len(nums):
            length+=1
            for i in range(len(nums)-length+1):
                if  maxv<sum(nums[i:i+length]):
                    maxv=sum(nums[i:i+length])
        return maxv
'''对于含有正数的序列而言,最大子序列肯定是正数,
所以头尾肯定都是正数.我们可以从第一个正数开始算起,
每往后加一个数便更新一次和的最大值;当当前和成为负数时,
则表明此前序列无法为后面提供最大子序列和,因此必须重新确定序列首项'''
    def maxSubArray2(self, nums):#代码简单，运行更快
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        #这里nums[i]的意思是在i之前包括i在内的最优子序列
        return max(nums)
    
