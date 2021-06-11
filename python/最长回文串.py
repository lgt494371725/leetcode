#虽然简单但细节很多
class Solution(object):
    def longestPalindrome(self, s):
        dic1={}
        dic1=dic1.fromkeys(s,0)
        for i in s:
            dic1[i]+=1
        length=0
        single=False
        for i in dic1:
            if dic1[i]%2==0:
                length+=dic1[i]
            if dic1[i]%2!=0:
                length+=dic1[i]-1
                single=True#这一步很重要
        return length+1 if single else length
