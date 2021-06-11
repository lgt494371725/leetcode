import tkinter as tk

class APP:
    def __init__(self,master):
        frame=tk.Frame(master)
        #框架用于将组件分组
        frame.pack(side=tk.LEFT,padx=10,pady=10)
        #自动调整位置，不输入参数则默认调整
        #pack(side=tk.LEFT,padx=10,pady=10)表示靠左边，离左边像素10，离上边像素10
        self.hi_there=tk.Button(frame,text="打招呼",fg="blue",command=self.say_hi)
        #会出现一个按钮，名为打招呼，字体为蓝色,fg就是设置字体颜色，bg是背景色
        #command是按下按钮之后的反馈
        self.hi_there.pack(padx=10,pady=10)
    def say_hi(self):
        print("互联网的广大朋友们大家好，我是小甲鱼！")
root=tk.Tk()
app=APP(root)

root.mainloop()
