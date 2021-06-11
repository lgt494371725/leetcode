#不能简单的判断有没有出现1次以上乱序
#2,4,1,3，尽管只有1次乱序，但1次改变是无法实现非递减的
class Solution(object):
    def checkPossibility(self, nums):
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                x,y=nums[i],nums[i-1]
                nums[i-1]=nums[i]
                if sorted(nums)==nums:
                    return True
                else:
                    nums[i-1]=y
                    nums[i]=nums[i-1]
                    return sorted(nums)==nums
#为什么需要赋值两次之后判断，考虑例子5,7,1,8和4，2，3
        return True

#更好的方法，减少了访问nums数组的次数
class Solution(object):
    def checkPossibility(self, nums):
        times=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                times+=1
                if times>1:#超过1次就是错
                    return False
                if i>1 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]
#这里是重点，当乱序时，5,7,1,8举例，如（7，1）要么变成(1,1)要么(7,7)
#变哪个要参考更前一个数据，显然应该变成77而不是11，
#423的情况，显然42->22，但由于前一个已经是经过点，不会影响之后的判断，所以可以不改
        return True

    
