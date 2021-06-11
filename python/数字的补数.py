class Solution(object):
    def findComplement(self, num):
        temp=num
        c=0
        #计算数字一共有几位，最后进行异或即可得反码
        while temp:
            temp>>=1
            c=(c<<1)+1
        return c^num

class Solution(object):
    def findComplement(self, num):
        return int(bin(num)[2:].\
                   replace('0', '2').replace('1', '0').replace('2', '1'), 2)
