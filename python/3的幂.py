#比想象中的难一些，不是能被3整除就是3的幂，用数学思维来想这个题
class Solution(object):
    def isPowerOfThree(self, n):
        if n<1:
            return False
        while n%3==0:
            n//=3
        return n==1
}
