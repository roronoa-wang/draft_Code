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
import tkinter.messagebox as m_box

# 窗口主题框架：
w = tk.Tk()
w.title("messagebox 弹窗")
w.geometry("500x500+200+30")

def hit_me():
    # m_box.showwarning(title="信息框",message="说明信息")
    # m_box.showwarning(title="警告框",message="警告warning")
    # m_box.showerror(title="错误",message="error错误")
    # print(m_box.askquestion(title="askquestion对话框",message="askquestion对话"))  # 返回值yes/no
    # print(m_box.askyesno(title="askyesno对话框",message="askyesno对话"))  # 返回值true/false
    # print(m_box.askokcancel(title="askokcancel对话框",message="askokcancel对话"))  # 返回值true/false
    print(m_box.askretrycancel(title="askretrycancel对话框",message="askretrycancel对话"))  # 返回值true/false

# 按钮：触发弹窗
tk.Button(w, text="各种弹窗", command=hit_me).pack()

w.mainloop()

