#判断是否是数字 isdigit()
#判断是否是字母 isalpha()
#判断是否是字母或数字 isalnum()
class Solution(object):
    def isPalindrome(self, s):
        s=''.join(ch.lower() for ch in s if ch.isalnum())
        return s==s[::-1]
