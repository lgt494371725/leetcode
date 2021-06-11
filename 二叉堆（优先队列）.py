class BinaryHeap:
    def __init__(self):
        self.heaplist=[0]#0号元素无意义
        self.currentsize=0
    def percup(self,i):
        while i//2>0:
            if self.heaplist[i]<self.heaplist[i//2]:
                self.heaplist[i],self.heaplist[i//2]=self.heaplist[i//2],self.heaplist[i]
            i//=2
    def insert(self,k):
        self.heaplist.append(k)#末尾加一
        self.currentsize=self.currentsize+1
        self.percup(self.currentsize)#新key上浮，调整到相应位置
    def delMin(self):
        retval=self.heaplist[1]
        self.heaplist[1]=self.heaplist[currentsize]
        self.currentsize-=1
        self.heaplist.pop()
        self.percdown(1)
        return retval
    def percdown(self,i):
        while (i*2)<=self.currentsize:
            if 2*i+1>self.currentsize:
                mc=2*i
            else:
                if self.heaplist[2*i]<self.heaplist[2*i+1]:
                    mc=2*i
                else:
                    mc=2*i+1
            if self.heaplist[i]>self.heaplist[mc]:
                self.heaplist[i],self.heaplist[mc]=self.heaplist[mc],self.heaplist[i]
            i=mc
    def buildheap(self,alist):
        i=len(alist)//2#从最后一棵子树开始构造
        self.currentsize=len(alist)
        self.heaplist=[0]+alist[:]
        print(len(self.heaplist),i)
        while(i>0):
            print(self.heaplist,i)
            self.percdown(i)
            i-=1
        print(self.heaplist,i)
        
