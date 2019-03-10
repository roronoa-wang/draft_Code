"""
导包：tkinter as tk
标签 和 按钮:
1，窗口主体框架：Windows窗口 + windows的一些属性 + 窗口内容 ，最后激活窗口
    主窗口：w = tk.Tk()
    主窗口的部分属性： w.title("窗口标题")
                       w.geometry("窗口尺寸500x500")
    激活窗口：w.mainloop()
2，窗口内容：标签、按钮
    小部件特性——标签：l = tk.Lable(主窗口windows, 属性..., 尺寸...textvariable=var1,text="xxxx")
    小部件特性——按钮：b = tk.Button(主窗口windows, 属性..., 尺寸...,按钮函数...command=函数)
    固定窗口位置： 小部件.pack()
3，文字存储器：
    var = tk.StringVar()  # 这时文字变量存储器
    var = tk.StringVar(value="bianliang")  # 这时文字变量存储器

"""
# 1，窗口主题框架：
import tkinter as tk

window = tk.Tk()
window.title("my windows")
# window.geometry("500x500")
window.geometry("500x500+500+100")
# 窗口内容-—标签1
# l = tk.Label(
#     window,  # 指定窗口
#     text='the lable in my window',  # 标签的文字
#     bg=('pink'),  # 标签的背景色
#     font=('Arial', 12),  # 字体和字体大小
#     width=50, height=5,  # 标签的尺寸
# )
# l.pack()  # 固定窗口的位置

var = tk.StringVar(value="bianliang")  # 这时文字变量存储器
# var= tk.StringVar()# 这时文字变量存储器
# 窗口内容-—标签2
l = tk.Label(
    window,
    textvariable=var,  # 使用textvarible 替换 text 因为这个可以变化
    bg='green',
    font=("Arial", 15),
    width=20, height=6
)
l.pack()

on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:  # 从False 状态变成 True
        on_hit = True
        var.set('you hit me')  # 设置标签的文字位“you hit me”
    else:
        on_hit = False  # 从False 状态变成 True
        var.set("")  # 设置文字位空来 达到隐藏效果
    return


# 窗口内容-—按钮
b = tk.Button(
    window,  # 指定窗口
    text="hit me",  # 显示在按钮上的文字
    width=15, height=2,
    command=hit_me  # 点击按钮时执行的命令，一般是函数之类的对象
)
b.pack()

window.mainloop()
