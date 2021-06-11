import turtle as t
t.title('自动轨迹绘制')
t.setup(800.600)
t.pencolor('red')
t.pensize(5)
datas[]
f=open('data.txt')
for line in f:
    line=line.replace("\n","")
    datas.append(list(map(eval,line.split(","))))
    #首先。split把整个字符串分解成独自的列表,map函数的功能是将第一个参数的功能作用于第二个参数的每一个元素，返回值需要类型转换
    #故这里用eval将列表里每个元素的引号都去掉了，变成了纯粹的数字，然后再列表化，最后将数字列表作为元素加入datas
f.close()
for i in range(len(datas)):
    t.pencolor(datas[i][3],datas[i][4],datas[i][5])
    #因为每行的后三个参数用于选择颜色
    t.fd(datas[i][0])
    if datas[i][1]:
        t.right(datas[i][2])
    else:
        t.left(datas[i][2])
