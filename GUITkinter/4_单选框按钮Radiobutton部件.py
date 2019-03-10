"""
导包：tkinter as tk
标签 和 按钮:
1，窗口主体框架：Windows窗口 + windows的一些属性 + 窗口内容 ，最后激活窗口
    主窗口：w = tk.Tk()
    主窗口的部分属性： w.title("窗口标题")
                       w.geometry("窗口尺寸widthxheight+x+y")
2，窗口内容(小部件)：文本框，输入框
    单选框部性——Radiobutton：Rb = tk.Radiobutton(w, text="Option A", variable=var1, value="A", command=print_selection)  生成一个单选框选项，N个就重复创建和Rb.pack()
        一个单选框选项算一个部件，
        # 其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
    固定窗口位置： 小部件.pack()
    
    标签部件补充：标签.config()  方法
        l.config(text='you have selected ' + var.get())


"""
import tkinter as tk

# 窗口主题框架：
w = tk.Tk()
w.title("单选框Radiobutton")
w.geometry("600x600+20+10")

# 文本存储器
var1 = tk.StringVar(value="empty")

# 标签部件：用于显示
l = tk.Label(w, bg="pink", width=50, text="empty")
l.pack()

# 事件函数
def print_selection():
    l.config(text='you have select ' + var1.get())

# Radiobutton单选框：
rb1 = tk.Radiobutton(w, text="Option A", variable=var1, value="A", command=print_selection)
# 其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
rb1.pack()

rb2 = tk.Radiobutton(w, text="Option B", variable=var1, value="B", command=print_selection)
# 其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
rb2.pack()

rb3 = tk.Radiobutton(w, text="Option C", variable=var1, value="C", command=print_selection)
# 其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
rb3.pack()

w.mainloop()
