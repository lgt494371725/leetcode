class Solution(object):
    def isSubsequence(self, s, t):
        i,j=0,0
        while i<len(s):
            if s[i] not in t[j:] or j>len(t)-1:
                return False
            j=t.index(s[i],j)+1
        #这里是关键点，不能用t[j:].index这种切片法，因为这边返回的坐标会重新从小的开始
            i+=1
        return True
class Solution:
    def isSubsequence(self, s, t):
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

    
