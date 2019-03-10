"""
导包：tkinter as tk
标签 和 按钮:
1，窗口主体框架：Windows窗口 + windows的一些属性 + 窗口内容 ，最后激活窗口
    主窗口：w = tk.Tk()
    主窗口的部分属性： w.title("窗口标题")
                       w.geometry("窗口尺寸widthxheight+x+y")
2，窗口内容(小部件)：文本框，输入框
    Scale尺度——Scale: s = tk.Scale(w, lable="pull me", from_=5, to=12, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01,command=print_selection)
        lable="pull me", 
        from_=5,  开始刻度
        to=12,   结束刻度
        orient=tk.HORIZONTAL, # 方向
        length=200,     # 参数length这里是指滚动条部件的长度，但注意的是和其他部件width表示不同，width表示的是以字符为单位，比如width=4，就是4个字符的长度，而此处的length=200，是指我们常用的像素为单位，即长度为200个像素
        showvalue=0,    是否显示当前刻度值，0 为不显示，1 为显示。
        tickinterval=2,     # 刻度显示间隔
        resolution=0.01,  # 分辨率，精度
        command=print_selection   事件函数
    
    固定窗口位置： 小部件.pack()
    
    标签部件补充：标签.config()  方法
        l.config(text="you have selected " + v)


"""
import tkinter as tk

# 窗口主题框架：

w = tk.Tk()
w.title("Scale 尺度")
w.geometry("500x500+100+50")

# 标签部件
l = tk.Label(w, bg="yellow", width=50, text="empty")
l.pack()

# 事件函数：
def print_selection(v):
    l.config(text="you have selected " + v)

# scale尺度 部件lv
s = tk.Scale(w, labe="pull me", from_=5, to=13, orient=tk.HORIZONTAL, length=200, showvalue=1,tickinterval=2, resolution=0.01,command=print_selection)
s.pack()

w.mainloop()
