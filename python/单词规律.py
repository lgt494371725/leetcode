class Solution(object):
    def wordPattern(self, pattern, s):
        str1=list(pattern)
        str2=s.split(' ')
        if len(str1)==1: return True
        if len(str1)!=len(str2): return False
        i=1 #只有1个就是对的
        dic1={}
        dic1[str1[0]]=str2[0]
        while i<len(str1):
            if str1[i] in dic1.keys():
                if str2[i]!=dic1[str1[i]]:
                    return False
            else:
                if str2[i] in dic1.values():
                    return False
            dic1[str1[i]]=str2[i]
            i+=1
        return True
