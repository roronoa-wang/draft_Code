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
w.title("Menubar 菜单")
w.geometry("500x500+200+30")

# 标签部件：
lb = tk.Label(w,bg="red",text="")
lb.pack()

counter = 0
def add_new_file():
    global counter
    lb.config(text="add " + str(counter) + " file")
    counter += 1


"""菜单栏部件："""
menubar = tk.Menu(w)   # 创建一个菜单栏
#   菜单栏的子元素：菜单页
filemenu = tk.Menu(menubar,tearoff=0)   # 创建菜单页子元素 ----- 菜单页   #  tk.Menu(filemenu)  表示：tk库中的 Menu 类 在 menubar 菜单栏上（）
menubar.add_cascade(label="file",menu=filemenu) # 在菜单栏上添加该菜单页
filemenu.add_command(label="New file",command=add_new_file) # 在菜单页上创建一个选项
filemenu.add_command(label="Open file",command=add_new_file) # 在菜单页上创建一个选项
filemenu.add_command(label="Save file",command=add_new_file) # 在菜单页上创建一个选项
filemenu.add_separator()    # 在菜单页中插入分割符
filemenu.add_command(label="Exit",command=w.quit) # 在菜单页上创建一个选项

editMenu = tk.Menu(menubar,tearoff=0)   # 创建菜单页子元素 ----- 菜单页
menubar.add_cascade(label="Edit",menu=editMenu) # 在菜单栏上添加该菜单页
editMenu.add_command(label="CUT",command=add_new_file) # 在菜单页上创建一个选项
editMenu.add_command(label="COPY file",command=add_new_file) # 在菜单页上创建一个选项
editMenu.add_command(label="PASTE file",command=add_new_file) # 在菜单页上创建一个选项
editMenu.add_separator()    # 在菜单页中插入分割符
editMenu.add_command(label="Exit",command=w.quit) # 在菜单页上创建一个选项

#  菜单页中的 子菜单页：
subMenu = tk.Menu(filemenu)  #  tk.Menu(filemenu)  表示：tk库中的 Menu 类 在 filemenu 菜单页上（）
filemenu.add_cascade(label="export",menu=subMenu,underline=0)
subMenu.add_command(label="Export txt",command=add_new_file)



# 将菜单栏部件放置主窗口上
w.config(menu=menubar)


w.mainloop()

