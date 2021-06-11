class Solution:
    def reverseBits(self, n):
        power=31
        num=0
        while n:
            num+=n%2<<power
            power-=1
            n/=2
        return num
