def sequantialsearch(alist,item):
    pos=0
    found=False
    while pos<len(alist) and not found:
        if alist[pos]==item:
            found=True
        else:
            pos+=1
    return found
#二分查找有多种写法,返回值是该数在数组中的位置，如果没有，返回的是插入点
def binarysearch(alist,item):#该算法最后start跟end不会重合
    start=0
    end=len(alist)-1
    while start<=end:#此处有等号,如果没这个等号，数组只有一个数或者剩下会有一个数被漏掉，如[2，2]
        mid=(start+end)//2#或者left+(end-start>>1)使用位运算更快，注意位运算优先级低于加减
#最好写成mid=start+(end-start)//2，因为start+end，如果两个数都很大，有溢出风险
        if alist[mid]==item:
            return mid
        else:
            if alist[mid]>item:
                end=mid-1
            else:
                start=mid+1
    return start
def searchInsert(nums,target):
    left,right=0,len(nums)#没有减一
    while left<right:#左闭右开
#该算法不能把right减一然后left<=right，这样的话会陷入死循环，因为最终left会等于right
        mid=left+(right-left)//2
        if nums[mid]<target:
#如果把<改成<=，则最终left会收敛到第一个大于target的数上，不改的话，最终则是收敛的一个不小于的数上
            left = mid+1
        else:#这里包括等于的情况，找到target后，不是立即返回，而是不断向左收缩
            right = mid
    return left#返回right也是一样的，位置重合

#https://www.cnblogs.com/kyoner/p/11080078.html
