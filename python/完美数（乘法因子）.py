import math
class Solution(object):
    def checkPerfectNumber(self, num):
        border=int(math.sqrt(num))
        sum1=0
        for i in range(1,border+1):
            if num%i==0:
                if i==num//i:
                    sum1+=i
                else: sum1+=i+num//i
        return sum1-num==num
