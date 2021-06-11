#脑筋急转弯
class Solution(object):
    def maxCount(self, m, n, ops):
        min1=m
        min2=n
        for i in ops:
            min1=min(min1,i[0])
            min2=min(min2,i[1])
        return min1*min2
