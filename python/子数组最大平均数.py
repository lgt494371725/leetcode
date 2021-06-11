#最简单的暴力法
class Solution(object):
    def findMaxAverage(self, nums, k):
        value=sum(nums[0:0+k])
        for i in range(1,len(nums)-k+1):
            if value<sum(nums[i:i+k]):
                value=sum(nums[i:i+k])
        return float(value)/k
#滑动窗口
class Solution(object):
    def findMaxAverage(self, nums, k):
        value=total=sum(nums[:k])
        for i in range(1,len(nums)-k+1):
            total=total-nums[i-1]+nums[i+k-1]
        #记住这里是total，不要用value带入，value是最大的情况下
            value=max(value,total)
        return float(value)/k
