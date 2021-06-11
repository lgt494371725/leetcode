class Solution(object):
    def singleNumber(self, nums):
        result=nums[0]
        for i in nums[1:]:
            result=result^i
        return result
    #具体看官方文档说明
