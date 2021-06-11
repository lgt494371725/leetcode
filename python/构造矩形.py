import math
class Solution(object):
    def constructRectangle(self, area):
        num=int(math.sqrt(area))
        dic1={}
        while num>0:
            if area%num==0:
                dic1[abs(num-area//num)]=[num,area//num]
            num-=1
        return sorted(dic1[min(dic1.keys())],reverse=True)
    #长宽顺序，大的在前
