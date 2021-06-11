#最开始写的
def findLHS(nums):
        dic1={}
        dic1=dic1.fromkeys(sorted(nums),0)
        for i in nums:
            dic1[i]+=1
        length=0
        alist=list(dic1.keys())
        for i in range(len(alist)):
            if i+1<len(alist) and abs(alist[i]-alist[i+1])==1:
                if dic1[alist[i]]+dic1[alist[i+1]]>length:
                    length=dic1[alist[i]]+dic1[alist[i+1]]
        return length
#更简洁
class Solution(object):
    def findLHS(self, nums):
        dic1={}
        dic1=dic1.fromkeys(nums,0)
        for i in nums:
            dic1[i]+=1
        length=0
        for i in dic1.keys():
            if dic1.get(i+1,None):
                length=max(length,dic1[i]+dic1[i+1])
        return length
