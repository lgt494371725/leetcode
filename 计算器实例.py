from tkinter import *

master=Tk()

frame=Frame(master)
frame.pack(padx=10,pady=10)
v1=StringVar()
v2=StringVar()
v3=StringVar()
def calc():
    result=int(v1.get())+int(v2.get())
    v3.set(str(result))
def  test(content):
    #content得到的是一个字符串类型,但不影响判断，如'123'.isdigit()还是会返回True
    return content.isdigit()
    #是数字为返回True，不是则返回False
testCMD=master.register(test) 
e1=Entry(frame,width=10,textvariable=v1,validate="key",\
         validatecommand=(testCMD,'%P')).grid(row=0,column=0)

Label(frame,text="+").grid(row=0,column=1)

e2=Entry(frame,width=10,textvariable=v2,validate="key",\
         validatecommand=(testCMD,'%P')).grid(row=0,column=2)
#key模式下，有任何输入都会直接调用验证函数，主有验证函数返回True，才会把内容放入输入框
#反之，如果返回的是False，内容则会自动清除
#所以此处不能有get函数，因为此时字母还没有进入输入框。只能用%P来实现获取内容
Label(frame,text="=").grid(row=0,column=3)
e3=Entry(frame,textvariable=v3,state="readonly").grid(row=0,column=4)
#输入框state共有三种：NORMAL--默认，re adonly--可以选中拷贝，但不可修改
#DISABLED--完全禁止。后两种状态下insert和delete方法是没用的
Button(frame,text="计算结果",command=calc).grid(row=1,column=2)

mainloop()
    
