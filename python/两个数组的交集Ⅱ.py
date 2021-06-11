#BIF
class Solution(object):
    def intersect(self, nums1, nums2):
        inter=set(nums1)&set(nums2)
        l=[]
        for i in inter:
            l+=[i]*min(nums1.count(i),nums2.count(i))
        return l
#哈希表
class Solution(object):
    def intersect(self, nums1, nums2):
        hashtable={}
        for i in nums1:
            if i in hashtable:
                hashtable[i]+=1
            else: hashtable[i]=1
        list1=[]
        for j in nums2:
            if j in hashtable and hashtable[j]!=0:
                list1.append(j)
                hashtable[j]-=1
        return list1
