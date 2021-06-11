class Solution(object):
    def findErrorNums(self, nums):
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                break
        gap=sum(nums)-sum(range(1,len(nums)+1))
        return [nums[i],nums[i]-gap]   
