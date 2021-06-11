#https://leetcode-cn.com/problems/repeated-substring-pattern/
#solution/zhong-fu-de-zi-zi-fu-chuan-by-leetcode-solution/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True
        return False
#简单的一种，看题解
class Solution(object):
    def repeatedSubstringPattern(self, s):
        return s in (s+s)[1:-1]
#如果掐头去尾后S仍包含在S+S字符串中，则说明该字符串可由子串组成
