class Solution(object):
    def removeElement(self, nums, val):
        if nums==[]: return 0
        i=0
        j=len(nums)-1
        while i<j:
            while i<j and nums[j]==val:
                j-=1
            while i<j and nums[i]!=val:
                i+=1
            if i<j :
                nums[i]=nums[j]
                j-=1#注意这里，i不能+1，不然i跟j可能不会归到同一位置，而是错开变成j<i
        return i if nums[i]==val else i+1
