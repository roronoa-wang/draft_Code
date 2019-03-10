"""
导包：tkinter as tk
标签 和 按钮:
1，窗口主体框架：Windows窗口 + windows的一些属性 + 窗口内容 ，最后激活窗口
    主窗口：w = tk.Tk()
    主窗口的部分属性： w.title("窗口标题")
                       w.geometry("窗口尺寸widthxheight+x+y")
2，窗口内容(小部件)：文本框，输入框
    小部件特性——Listbox列表部件：lb = tk.Listbox(主窗口windows, 属性..., 尺寸..., listvariable=var2)  其中var2是一个序列类型
        插入：lb.insert(位置, 值)   位置从0开始
        删除：lb.delete(位置)
    固定窗口位置： 小部件.pack()
3，文字存储器：
    var = tk.StringVar()  # 这时文字变量存储器
    var = tk.StringVar(value="bianliang")  # 这时文字变量存储器
    var.set(value=v)  # v = xxx
"""
import tkinter as tk
# 窗口主题框架：
w = tk.Tk()
w.title("List列表部件")
w.geometry("500x500")

# 文本存储器StringVar()
var1 = tk.StringVar()
# 标签部件：用于显示
lb = tk.Label(w,bg='yellow', width=5, textvariable=var1)
lb.pack()

# 创建事件（函数）：用于点击
def print_selection():
    value = lb.get(lb.curselection()) # 获取当前选中的文本
    var1.set(value=value)  # 为lable设置值

# 按钮部件:
bt = tk.Button(w, text="print select", width=15, height=2, command=print_selection)
bt.pack()



# Listbox部件 和 文本存储器2StringVar()
# 文本存储器StringVar()
var2 = tk.StringVar()
var2.set(value=(11,22,33,44))  # 为变量设置值

# 创建Listbox
lb = tk.Listbox(w, listvariable=var2)  # 将 var2 的值赋给Listbox
# 创建一个list并将值循环添加到Listbox控件中
list_items = [1,2,3,4]
# for i in list_items:
#     lb.insert("end",i)  # 从最后一个位置开始加入值insert_value

# 创建事件（函数）：用于点击
def insert_value():
    for i in list_items:
        lb.insert("end", i)  # 从最后一个位置开始加入值insert_value
# 按钮部件:
bt = tk.Button(w, text="insert_value", width=15, height=2, command=insert_value)
bt.pack()

lb.insert(0,"first")  # 在第1个位置加入‘first’字符  位置从0 开始算
lb.insert(1,"second")  # 在第2个位置加入‘second’字符
lb.delete(2)  # 删除第2个位置的字符
lb.pack()

w.mainloop()