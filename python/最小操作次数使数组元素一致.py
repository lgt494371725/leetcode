#重要的是数学的思考
class Solution(object):
    def minMoves(self, nums):
        minv=min(nums)
        sum1=0
        for i in nums:
            sum1+=i-minv
        return sum1
