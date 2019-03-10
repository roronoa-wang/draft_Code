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

""" pack() 放置"""
# tk.Label(w,text="top",bg="blue",width=20,height=6).pack(side="top")
# tk.Label(w,text="left",bg="blue",width=20,height=6).pack(side="left")
# tk.Label(w,text="bottom",bg="blue",width=20,height=6).pack(side="bottom")
# tk.Label(w,text="right",bg="blue",width=20,height=6).pack(side="right")

""" grid() 放置"""
# for i in range(4):
#     for j in range(3):
#         # tk.Label(w, text="grid",bg="pink").grid(row=i,column=j)
#         # tk.Label(w, text="grid",bg="pink").grid(row=i,column=j, padx=10,pady=10)
#         # tk.Label(w, text="grid",bg="pink").grid(row=i,column=j, ipadx=10,ipady=10)
#         tk.Label(w, text="第"+str(i+1)+"行第"+str(j+1)+"列",bg="pink").grid(row=i,column=j, padx=15,pady=15,ipadx=15,ipady=15)

""" place() 放置  anchor参数：部件的锚点----上北下南左西右东，东西南北的英文首字母小写，x和y是部件在窗口的位置"""
tk.Label(w,text="北",bg="yellow").place(x=100,y=100,anchor="n")
tk.Label(w,text="南",bg="yellow").place(x=100,y=100,anchor="s")
tk.Label(w,text="东",bg="yellow").place(x=100,y=100,anchor="e")
tk.Label(w,text="西",bg="yellow").place(x=100,y=100,anchor="w")

w.mainloop()

