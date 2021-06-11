class Solution(object):
    def hammingDistance(self, x, y):
        x=x&(2**31-1)
        y=y&(2**31-1)
        z=1&(2**31-1)
        distance=0
        for i in range(31):
            x1=x&z
            y1=y&z
            distance+=x1^y1
            x>>=1
            y>>=1
        return distance
