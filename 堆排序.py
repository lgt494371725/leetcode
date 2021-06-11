alist=[9,0,5,8,2,4,6,3,5,10]


def heap_sort(nums):
    length = len(nums)
    for i in range(length//2, -1, -1):
        heap_ajust(nums, i, length-1)
    for i in range(length-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heap_ajust(nums, 0, i-1)
    return nums


def heap_ajust(nums, root, end):
    temp = nums[root]
    pos = 2*root+1
    while pos <= end:
        if pos < end and nums[pos] < nums[pos+1]:
            pos += 1
        if temp >= nums[pos]:
            pos *= 2
            break
        else:
            nums[root] = nums[pos]
            root = pos
            pos*=2
    nums[root] = temp
