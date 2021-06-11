import turtle as t
def koch(size,n):
    if n==0:
        t.fd(size)
    #如果是0阶，就绘制一条直线
    else:
        for angle in [0,60,-120,60]:#四个角度代表科赫曲线的四条线段
            t.left(angle)
            koch(size/3,n-1)

def main():
    t.setup(800,800)
    t.penup()
    t.goto(-300,-50)
    t.pendown()
    t.pensize(2)
    level=1
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.hideturtle()
    
main()
