class Solution:
    def singleNumber(self, nums) :
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:#total要么0要么1
                # Python 这里对于最高位需要特殊判断
#由于python中是由补码存储的，若高位为1，则需把ans转换为补码对应的数字
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans
