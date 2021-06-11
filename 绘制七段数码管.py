from turtle import *
import time
def drawGap():#希望数字每条线之间有间隔
    penup()
    fd(5)
def drawLine(draw):#绘制单段数码管
    drawGap()
    pendown() if draw else penup()
    fd(40)
    drawGap()
    right(90)
    #真就画非真就飞过
def drawDigit(digit):#该函数根据digit绘制对应的七段管数字
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    #比如如果数字是0，第一条线就不用绘制，所以不在判断里
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    #此时连续右转四次，海龟回到原点且方向朝右，想要绘制七段，需转向
    left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,5,6,7,8,9] else drawLine(False)
    left(180)#使海龟方向朝右
    penup()
    fd(20)#为后续数字确定位置
def drawDate(date):#date为日期，约定格式为'%Y-%m=%d+'
    pencolor('red')
    for i in date:
        if i =='-':
            write('年',font=('Arial',18,'normal'))#字体，字号大小
            pencolor('green')
            fd(40)
        elif i=='=':
            write('月',font=('Arial',18,'normal'))
            pencolor('blue')
            fd(40)
        elif i=='+':
            write('日',font=('Arial',18,'normal'))
        else:
            drawDigit(eval(i))#因为是字符类型所以要去掉引号
def main():
    setup(800,350,200,200)
    penup()
    fd(-300)
    pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    hideturtle()
    #在图形完成后会隐藏画笔的turtle形状
    done()

main()
 
