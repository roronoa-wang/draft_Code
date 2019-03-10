"""
导包：tkinter as tk
标签 和 按钮:
1，窗口主体框架：Windows窗口 + windows的一些属性 + 窗口内容 ，最后激活窗口
    主窗口：w = tk.Tk()
    主窗口的部分属性： w.title("窗口标题")
                       w.geometry("窗口尺寸500x500")
2，窗口内容(小部件)：文本框，输入框
    小部件特性——文本框：t = tk.Text(主窗口windows, [属性...,] [尺寸...])
        t.issert(index,var)：将var值插入到文本框中的index位置
    小部件特性——输入框：e = tk.Entry(主窗口windows, [属性...,] {尺寸...])
        e.get():获取输入框的内容
    固定窗口位置： 小部件.pack()
def insert_point():
    var = e.get()
    t.insert("insert",var)
"""
import tkinter as tk
# 窗口主题框架：
w = tk.Tk()
w.title("Entry&Text")
w.geometry("500x500+500+100")

def insert_point():
    var = e.get()
    t.insert("insert",var)

def insert_end():
    var = e.get()
    t.insert("end",var)

def insert_head():
    var = e.get()
    t.insert("0",var)

# 输入框：用户输入的内容显示为 * 号
e = tk.Entry(w)
e.pack()
# 按钮：分别触发两种情况
b1 = tk.Button(w, text="insert point", width=15,height=2, command=insert_point)
b1.pack()

b2 = tk.Button(w, text="insert end", width=15,height=2, command=insert_end)
b2.pack()

b3 = tk.Button(w, text="insert head", width=15,height=2, command=insert_head)
b3.pack()

# 文本框：用于显示
t = tk.Text(w, height=2)
t.pack()

w.mainloop()