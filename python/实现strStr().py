class Solution(object):
    def strStr(self, haystack, needle):
        if needle=='': return 0
        if haystack=='' :return -1
        i,j=len(haystack),len(needle)
        k=0
        while k+j<=i:
            if haystack[k:k+j]==needle:
                return k
            k+=1
        return -1
