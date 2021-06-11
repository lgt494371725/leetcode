#复杂度较高的做法
class Solution(object):
    def longestPalindrome(self, s):
        for i in range(len(s), 0,-1):
            for start in range(0, len(s)-i+1):
                temp = s[start:start+i]
                if temp == temp[::-1]:
                    return temp
#稍微快一些，总复杂度还是偏高
class Solution(object):
    def longestPalindrome(self, s):
        for i in range(len(s), 0,-1):
            for start in range(0, len(s)-i+1):
                left = start
                right = left+i-1
                while left < right:
                    if s[left] != s[right]:
                        break
                    left+=1
                    right-=1
                else:
                    return s[start:start+i]
#快很多O(n^2)
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s) :
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]



    
