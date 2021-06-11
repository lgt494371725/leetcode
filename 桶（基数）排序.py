alist=[9,0,5,8,2,4,6,3,5,10]


def radix_sort(nums):
    maxnum = max(nums)
    looptimes = 0
    while maxnum:
        looptimes += 1
        maxnum //= 10
    for i in range(looptimes):
        nums = sort_helper(nums, i)
    return nums


def sort_helper(nums, digit):
    dic1 = {i:[] for i in range(10)}
    for i in nums:
        index = (i//10**digit)%10
        dic1[index].append(i)
    nums = []
    nums.extend(j for i in range(10) for j in dic1[i])
    return nums
