class Solution(object):
    def reverse(self, x):
        res=0
        a=abs(x)#必须取绝对值。因为负数不能直接用求余和整除命令
        while(a!=0):
            res=res*10+a%10
            if res>(1<<31)-1 or res<-(1<<31):
                return 0
            a//=10
        return res if x>0 else -res
