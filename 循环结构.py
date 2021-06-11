#遍历循环
#计数循环 for i in range(1,5)-->i=1,2,3,4
#for i in range(1,6,2)--->i=1,3,5
#字符串遍历循环 for c is s: 遍历字符串每个字符
for c in "Pyhthon123":
    print(c,end=',')
#列表遍历循环 for item in ls: ls是列表
print('\n')
for item in [123,'PY',456]:
    print(item,end=' ')
#无限循环
a=3
while a>0:
    a=a-1
    print(a)
#break：跳出并结束当前循环 continue：结束当次循环，继续后续循环
for c in range(4):
    if c==1:
        continue
    print(c,end='')
#可以将else和循环联合使用，当循环中不出现break时，就执行else语句
print('\n')
for i in range(2):
    print('1')
else:
    print('正常退出')
