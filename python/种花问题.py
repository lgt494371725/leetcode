#这题比想象中的难
#要考虑到除了原有的花，新的花种下后也会产生新的种植禁区
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        i=0
        while i<len(flowerbed):
            if flowerbed[i]==1 or flowerbed[i]==-1:pass
            else:
                if i==0 or (i>0 and flowerbed[i-1]!=1):
                    if i==len(flowerbed)-1 or (i<len(flowerbed)-1 and flowerbed[i+1]!=1):
                        n-=1
        #在i处是应该是要种植的。但这里通过给两边赋予禁区跳过了赋值操作
                        if i>0:
                            flowerbed[i-1]=-1
        #用了新的值-1，这是新的禁区
                        if i<len(flowerbed)-1:
                            flowerbed[i+1]=-1
            i+=1
        return n<=0
#一个重要的技巧！防御式编程思想，在数组两端各增加一个0
#这样就可以避免麻烦的边界条件判断
#更简洁的方法
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed=[0]+flowerbed+[0]
        for i in range(1,len(flowerbed)-1):
    #注意这里range的取法，因为前后增加了0，所以索引值也要调整，数组的第一个值此时在1位置
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                flowerbed[i]=1
                n-=1
        return n<=0
