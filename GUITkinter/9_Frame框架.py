"""
导包：tkinter as tk
标签 和 按钮:
1，窗口主体框架：Windows窗口 + windows的一些属性 + 窗口内容 ，最后激活窗口
    主窗口：w = tk.Tk()
    主窗口的部分属性： w.title("窗口标题")
                       w.geometry("窗口尺寸widthxheight+x+y")
2，窗口内容(小部件)：文本框，输入框
    菜单 —— Menubar:
    Menubar的方法之一：
    固定窗口位置： 小部件.pack()
 


"""
import tkinter as tk

# 窗口主题框架：
w = tk.Tk()
w.title("Frame 框架！！！")
w.geometry("600x600+300+50")

# 标签部件：
lb = tk.Label(w,bg="red",text="on the windows --- w")
lb.pack()

# 框架部件：相当于容器。   可以理解主窗口时一个特殊的大容器
# fm = tk.Frame(w,background="blue",width=60,height=60)
# fm = tk.Frame(w,background="blue")
# fm.pack()

# # 在 fm 容器中 再创建 frame 容器
# fm_1 = tk.Frame(fm,background="pink")
# fm_2 = tk.Frame(fm)
#
# fm_1.pack(side="left")
# fm_2.pack(side="right")
#
# # 在这里的三个label 就是在我们创建的的frame上定义的label部件，还是以容器理解，就是容器上贴上标签，来指明解释这个容器
# lb_fm = tk.Label(fm,text="on the fm")
# lb_fm_1 = tk.Label(fm_1,text="on the fm_1")
# lb_fm_2 = tk.Label(fm_2,text="on the fm_2")
#
# lb_fm.pack()
# lb_fm_1.pack()
# lb_fm_2.pack()

# 框架部件：相当于容器。   可以理解主窗口时一个特殊的大容器
fm = tk.Frame(w,background="pink",width=600,height=500)
fm.pack()


w.mainloop()

