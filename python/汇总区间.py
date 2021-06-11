class Solution(object):
    def summaryRanges(self, nums):
        i=0
        list1=[]
        while i<len(nums):
            j=i+1
            while j<len(nums) and nums[j]-nums[j-1]==1:
                j+=1
            list1.append(str(nums[i]) if j-i==1 else "{}->{}".format(nums[i],nums[j-1]))
            i=j
        return list1
