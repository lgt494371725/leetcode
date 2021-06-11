from tkinter import *
import webbrowser

root=Tk()
text=Text(root,width=30,height=5)
text.pack()

text.insert(INSERT,"I LOVE FISHC.com")
text.tag_add("link","1.7","1.16")
text.tag_config("link",foreground="blue",underline=True)

def show_arrow_cursor(event):
    text.config(cursor="arrow")

def show_xterm_cursor(event):
    text.config(cursor="xterm")

def click(event):
    webbrowser.open("http://www.fishc.com")


    
text.tag_bind("link","<Enter>",show_arrow_cursor)
#Enter.cursor表示鼠标放在该标签上时，会显示arrow即箭头形状，Leave表示不在标签上时的形状。
text.tag_bind("link","<Leave>",show_xterm_cursor)
text.tag_bind("link","<Button-1>",click)
#button-1代表鼠标左键点击，会触发click函数
