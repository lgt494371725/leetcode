#与字符串相加的解法是一样的，只需把2改成10
class Solution(object):
    def addBinary(self, a, b):
        a=list(a[::-1])
        b=list(b[::-1])
        a=map(int,a)
        b=map(int,b)
        length=len(a) if len(a)<len(b) else len(b)
        carry=0
        for i in range(length):
            result=(a[i]+b[i]+carry)%2
            carry=(a[i]+b[i]+carry)//2
            a[i]=result
        if len(a)>len(b):
            while i+1<len(a) and carry==1:
                i+=1
                result=(a[i]+1)%2
                carry=(a[i]+1)//2
                a[i]=result
            if carry==1:
                a.append('1')
        else:
            a=a+b[i+1:]
            while i+1<len(a) and carry==1:
                i+=1
                result=(a[i]+1)%2
                carry=(a[i]+1)//2
                a[i]=result
            if carry==1:
                a.append('1')
        a=map(str,a)
        a=''.join(a)
        a=a[::-1]
        return a
#第二种，简单很多，用这个
class Solution(object):
    def addStrings(self, a, b):
        s=[]
        carry,i,j=0,len(a)-1,len(b)-1
        while i>=0 or j>=0 or carry!=0:
            if i>=0: 
                carry+=int(a[i])
                i-=1
            if  j>=0:
                carry+=int(b[j])
                j-=1
            s.insert(0,str(carry%10))
            carry//=10
        return ''.join(s)
