def Narcissus():
    for each in range(100,1000):
        temp=each
        sum=0
        for i in range(0,3):
            sum=sum+((temp//(10**i))%10)**3
        if sum==each:
            print(each,end='\t')

print("所有的水仙花是分别是：",end='')
Narcissus()
