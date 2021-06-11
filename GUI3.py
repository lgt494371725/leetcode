import tkinter as tk

root=tk.Tk()
test=tk.Label(root,text="测试内容显示")
test.pack(side=tk.LEFT,padx=20)
photo=tk.PhotoImage(file="D://C//123.gif")
#不支持jpg
imgLable=tk.Label(root,image=photo)
imgLable.pack(side=tk.RIGHT)

root.mainloop()
'''from tkinter import*
root=Tk()
test=Label(root,text="xxxxx")
test.pack(xx)
photo=PhotoImage(xxx)
imgLabel=Label(root,xx)
'''
