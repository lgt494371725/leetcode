def SelectSort(alist):
    end=len(alist)-1
    while end>0:
        maxpos=end
        for i in range(end):
            if alist[i]>alist[maxpos]:
                maxpos=i
        alist[end],alist[maxpos]=alist[maxpos],alist[end]
        end-=1
    return alist

def BubbleSort(alist):
    end=len(alist)-1
    while end>0:
        for i in range(end):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
        end-=1
    return alist
def InsertSort(alist):
    for index in range(1,len(alist)):
        if alist[index-1]>alist[index]:
            temp=alist[index]
            while temp<alist[index-1] and index>0:
                alist[index]=alist[index-1]
                index-=1
            alist[index]=temp
    return alist
def ShellSort(alist):
    gap=len(alist)//2
    while gap>0:
        for divide in range(gap):
            for index in range(divide+gap,len(alist),gap):
                if alist[index-gap]>alist[index]:
                    temp=alist[index]
                    while temp<alist[index-gap] and index>=gap:#注意这里index>=gap很重要,index-gap一定要大于等于0才有意义
                        alist[index]=alist[index-gap]
                        index-=gap
                    alist[index]=temp
        gap//=2
    return alist

def mergeSort(alist):
    if len(alist)>1:
        mid=len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i <len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i+=1
            else:
                alist[k]=righthalf[j]
                j+=1
            k+=1
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i+=1
            k+=1
        while j<len(righthalf):
            alist[k]=righthalf[j]
            j+=1
            k+=1
    return alist
def mergeSort2(alist):#优化版
    if len(alist)<=1:
        return alist
    middle=len(alist)//2
    left=mergeSort2(alist[:middle])
    right=mergeSort2(alist[middle:])
    merged=[]
    while left and right:
        if left[0]<=right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint=partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)
def partition(nums, start, end):
    value = nums[start]
    while start < end:
        while start < end and value < nums[end]:
            end-=1
        nums[start] = nums[end]
        while start < end and value > nums[start]:
            start+=1
        nums[end] = nums[start]
    nums[start] = value
    return start

a=[54,26,93,17,77,56,44,55,20]
quickSort(a)
print(a) 






            
