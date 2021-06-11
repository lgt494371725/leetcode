class Solution(object):
    def findDisappearedNumbers(self, nums):
        len1=len(nums)
        nums=sorted(set(nums))
        gap=len1-len(nums)
        list1=[]
        pos=0
        for i in range(1,len1+1):
            if gap==0:
                break
            if pos>=len(nums) or i != nums[pos]:#注意这里，防止越界需要两个判断
                list1.append(i)
                gap-=1#为减少循环次数
            else: pos+=1
        return list1

#更好的方法，空间复杂度小
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Iterate over each of the elements in the original array
        for i in range(len(nums)):
            
            # Treat the value as the new index
            new_index = abs(nums[i]) - 1
            
            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative 
            # thus indicating that the number nums[i] has 
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array 
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
                
        return result
#https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/solution/zhao-dao-suo-you-shu-zu-zhong-xiao-shi-de-shu-zi-2/
