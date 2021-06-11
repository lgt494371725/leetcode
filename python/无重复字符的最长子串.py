class Solution(object):
    def lengthOfLongestSubstring(self, s):
        tail = 0
        alist = []
        maxlength = 0
        while tail < len(s):
            while tail < len(s) and s[tail] not in alist:
                alist.append(s[tail])
                tail += 1
            maxlength = max(maxlength,len(alist))
            if tail == len(s): break
            while alist.pop(0) != s[tail]:
                pass 
        return maxlength
