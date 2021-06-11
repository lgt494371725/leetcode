class Solution(object):
    def countAndSay(self, n):
        str1="1"
        while n>1:#记得要重置参数
            count=1
            i=0
            length=len(str1)
            str2=str1[:]
            str1=""
            while i <length:
                while i+1<length and str2[i]==str2[i+1]:
                    count+=1
                    i+=1
                str1=str1+str(count)+str2[i]
                count=1
                i+=1
            n-=1
        return str1
