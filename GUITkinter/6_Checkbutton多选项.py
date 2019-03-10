"""
导包：tkinter as tk
标签 和 按钮:
1，窗口主体框架：Windows窗口 + windows的一些属性 + 窗口内容 ，最后激活窗口
    主窗口：w = tk.Tk()
    主窗口的部分属性： w.title("窗口标题")
                       w.geometry("窗口尺寸widthxheight+x+y")
2，窗口内容(小部件)：文本框，输入框
    勾选框（多选框）——Checkbutton：有点类似单选框
        cb1 = tk.Checkbutton(w, text="Python", variable=var1, onvalue=1, offvalue=0, command=print_selection)
        多选框每个部件都要一个文本存储器（而单选框只要一个），且多选框有选中和未选中的参数onvalue=1, offvalue=0,
    固定窗口位置： 小部件.pack()
    
    标签部件补充：标签.config()  方法
        l.config(text="you have selected " + v)


"""
import tkinter as tk

# 窗口主题框架：
w = tk.Tk()
w.title("多选框 Checkbutton")
w.geometry("500x500+200+50")

# 标签部件--用于显示
l = tk.Label(w, bg="pink", width=20, text="empty")
l.pack()


# 触发事件函数
def print_selection():
    if (var1.get() == 1) & (var2.get() == 1):   #如果两个选项都选中
        l.config(text="I love both")
    elif (var1.get() == 1) & (var2.get() == 0): #如果选中第一个选项，未选中第二个选项
        l.config(text="I love only Python")
    elif (var1.get() == 0) & (var2.get() == 1): #如果未选中第一个选项，选中第二个选项
        l.config(text="I love only Java")
    else:
        l.config(text="I don't love either")

# 多选框 Ckeckbutton
var1 = tk.IntVar()
cb1 = tk.Checkbutton(w, text="Python", variable=var1, onvalue=1, offvalue=0, command=print_selection)
cb1.pack()

var2 = tk.IntVar()
cb2 = tk.Checkbutton(w, text="Java", variable=var2, onvalue=1, offvalue=0, command=print_selection)
cb2.pack()


w.mainloop()
