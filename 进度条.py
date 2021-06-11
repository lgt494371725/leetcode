#进度条
import time
print("------执行开始-------")
scale=10
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结束-------")
#单行动态刷新
import time
for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.1)
#/r表示在打印输出之前，光标会退回行首
#逗号后面的是print函数的参数，让print函数输出字符串后也不会换行
#可以在end="x"的x处增加任意参数，将会被打印出来
#在IDLE的开发环境中显示出的效果并不是单行刷新，但程序是没有问题的

#综合以上的程序
def f(x):
    return pow(x+(1-x)*0.03,2)
import time
scale=50
print("执行开始".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    #想利用不同速度的函数把i/scale改成f(i/scale)即可
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,f(dur)),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-')) 
