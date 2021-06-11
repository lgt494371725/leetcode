from turtle import *

def sierpinski(degree,points):
    #points是包含点的字典类型，描绘了三角形的轮廓，左下角，顶，和右边三个点的坐标
    colormap=['blue','red','green','white','yellow','orange']
    drawTriangle(points,colormap[degree])
    if degree>0:
        #减小规模，getmid取中点，边长减半（画图可知），调用自身，左-上-右
        sierpinski(degree-1,{'left':points['left'],'top':getMid(points['left'],points['top']),'right':getMid(points['left'],points['right'])})
        sierpinski(degree-1,{'left':getMid(points['left'],points['top']),'top':points['top'],'right':getMid(points['top'],points['right'])})
        sierpinski(degree-1,{'left':getMid(points['left'],points['right']),'top':getMid(points['top'],points['right']),'right':points['right']})

def drawTriangle(points,color):
    t.fillcolor(color)
    #绘制图形的填充颜色
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    #准备开始填充
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()
    #填充完成
def getMid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
t=Turtle()
points={'left':(-200,-100),'top':(0,200),'right':(200,-100)}
sierpinski(5,points)

done()
