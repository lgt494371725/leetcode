#随机函数random库
#基本随机函数：seed(),random()
#random(),生成一个0到1时间的随机小数
import random
random.seed(10)
a=random.random()
b=random.random()
print(a,b)
#可以不设定种子，如果想要复现整个过程，可以设定种子
random.seed(10)#在此处重新调用种子，则随机数会重现，即a和c的值会相同
c=random.random()
#random.randint(a,b) 随机生成一个ab之间的整数
#range.randrange(m,n,k) 生成mn之间以k为步长的整数
#uniform(a,b)生成ab之间的随机小数
#getrandbits(k) 生成一个k比特长的随机整数
#random.choice([1,2,3,4])从序列中随机选择一个元素
#random.shuffle([1,2,3,4])随机打乱序列
