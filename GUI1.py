import tkinter as tk

app=tk.Tk()
#'实例化'
app.title("FishC Demo")

theLabel=tk.Label(app,text='我的第二个窗口程序！')
#'用于显示文本，图标，图片'
theLabel.pack(side=tk.LEFT,padx=10,pady=100)
#'用于自动调节组件的尺寸和位置'

app.mainloop()
#'使窗口出现'
