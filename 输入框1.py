from tkinter import *
root=Tk()

Label(root,text="作品：").grid(row=0,column=0)
Label(root,text="作者：").grid(row=1,column=0)

e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)

def show():
    print("作品：{}".format(e1.get()))
    print("作者：{}".format(e2.get()))
    #通过get函数获取输入框内容
    e1.delete(0,END)
    e2.delete(0,END)

Button(root,text="获取信息",width=10,command=show)\
        .grid(row=3,column=0,sticky=W,padx=10,pady=5)
Button(root,text="退出",width=10,command=root.quit)\
        .grid(row=3,column=1,sticky=E,padx=10,pady=5)
#root.quit表示退出程序,sticky设置方向

mainloop()
