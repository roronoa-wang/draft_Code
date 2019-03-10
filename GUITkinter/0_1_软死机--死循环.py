import tkinter as tk
import tkinter.messagebox as m_box
import time

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
    print(m_box.askretrycancel(title="askretrycancel对话框", message="askretrycancel对话"))  # 返回值true/false


def endless_loop():
    while True:
        time.sleep(3)


# 按钮：触发弹窗
tk.Button(w, text="死循环", command=endless_loop).pack()
tk.Button(w, text="各种弹窗", command=hit_me).pack()

w.mainloop()
