#法一，判断（2,x-1）是否是数x的因子
#根据规律，只需检查（2,根号x）即可
#更好的方法：埃氏筛，详情看题解
class Solution(object):
    def countPrimes(self, n):
        isprime=[0 for i in range(n)]
        ans=0
        for i in range(2,n):
            if isprime[i]==0: ans+=1
            j=i
            while j*i<n:
                isprime[j*i]=1
                j+=1
        return ans
