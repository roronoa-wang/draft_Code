"""
"""
# import tkinter as tk
#
# # 窗口主题框架：
# w = tk.Tk()
# w.title("Frame 框架！！！")
# w.geometry("600x600+300+50")
#
# # 标签部件：
# lb = tk.Label(w,bg="red",text="on the windows --- w")
# lb.pack()
#
#
# # # 在 fm 容器中 再创建 frame 容器
# # fm_1 = tk.Frame(fm,background="pink")
# # fm_2 = tk.Frame(fm)
# #
# # fm_1.pack(side="left")
# # fm_2.pack(side="right")
# #
# # # 在这里的三个label 就是在我们创建的的frame上定义的label部件，还是以容器理解，就是容器上贴上标签，来指明解释这个容器
# # lb_fm = tk.Label(fm,text="on the fm")
# # lb_fm_1 = tk.Label(fm_1,text="on the fm_1")
# # lb_fm_2 = tk.Label(fm_2,text="on the fm_2")
# #
# # lb_fm.pack()
# # lb_fm_1.pack()
# # lb_fm_2.pack()
#
# # 框架部件：相当于容器。   可以理解主窗口时一个特殊的大容器
# fm = tk.Frame(w,background="pink",width=600,height=500)
# fm.pack()
#
#
# w.mainloop()

import tkinter
from pydoc import browse
from  tkinter import ttk  # 导入内部包

"""
https://docs.python.org/3/library/tkinter.ttk.html#treeview
https://cloud.tencent.com/developer/ask/174526
"""

# 触发事件函数
def print_selection():
    pass


# 多选框 Ckeckbutton
# var1 = tkinter.IntVar()
# cb1 = tkinter.Checkbutton(tree, text="Python", variable=var1, onvalue=1, offvalue=0, command=print_selection)
# cb1.pack()

win = tkinter.Tk()

# tree = ttk.Treeview(win, selectmode=extend)  # 表格
tree = ttk.Treeview(win)  # 表格

tree["columns"] = ("姓名", "年龄", "身高")
tree.column("姓名", width=100)  # 表示列,不显示
tree.column("年龄", width=100)
tree.column("身高", width=100)

tree.heading("姓名", text="姓名-name")  # 显示表头
tree.heading("年龄", text="年龄-age")
tree.heading("身高", text="身高-tall")

l1 = tree.insert("", 0, text="line1", values=("1", "2", "3"))  # 插入数据，
tree.insert("", 1, text="line1", values=("1", "2", "3"))
tree.insert("", 2, text="line1", values=("1", "2", "3"))
tree.insert("", 3, text="line1", values=("1", "2", "3"))

# print(l1.iid)
print(tree.focus(l1))

# print(tree.selection)

tree.pack()

win.mainloop()
