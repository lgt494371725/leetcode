class Solution(object):
    def removeDuplicates(self, nums):
        if nums==[]: return 0
        i,j=0,1
        while j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                nums[i+1]=nums[j]
                j+=1
                i+=1
        return i+1
