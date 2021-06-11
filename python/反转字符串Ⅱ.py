class Solution(object):
    def reverseStr(self, s, k):
        i=0
        news=''
        reverse=True
        while i<len(s):
            if reverse and i+k>=len(s):
                news+=s[i:][::-1]#
            elif reverse:
                news+=s[i:i+k][::-1]
                #这里一定要注意不要写成s[i:i+k:-1]
                #因为你这样写的时候坐标是从右到左开始计算的，和你想的不同
                reverse=False
            elif not reverse: 
                news+=s[i:i+k]
                reverse=True
            i+=k
        return news
