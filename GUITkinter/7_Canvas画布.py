"""
导包：tkinter as tk
标签 和 按钮:
1，窗口主体框架：Windows窗口 + windows的一些属性 + 窗口内容 ，最后激活窗口
    主窗口：w = tk.Tk()
    主窗口的部分属性： w.title("窗口标题")
                       w.geometry("窗口尺寸widthxheight+x+y")
2，窗口内容(小部件)：文本框，输入框
    画布 —— Canvas:c1 = tk.Canvas(w, bg="blue", height=200,width=400)  单位为像素，其他参数含义与其他部件一样
    画布的方法之一：canvas.mmove(子元素,x,y)  # x 为x 方向上的移动的距离，y 类似 x
    固定窗口位置： 小部件.pack()
 
    画布的子元素： 
        图片存储器（类似变量存储器） --- PhotoImage():image_file= tk.PhotoImage(file="ins.gif")  file 为文件路径
            用于存放 ins.gif 这张 图片
        
        粘贴图片：
            canvas.create_image(10, 10, anchor='nw', image=image_file)， 前三个参数确定图片与画布的位置
            里面的参数10,10就是图片放入画布的坐标，
            而这里的anchor=nw则是把图片的左上角作为锚定点，在加上刚刚给的坐标位置，即可将图片位置确定。
            n --- 上，w --- 左， e --- 右， s --- 下，center --- 中间 （上北下南左西右东）
        
        粘贴线条（画一条直线）：
            x0, y0, x1, y1 = 50, 50, 80, 80
            line1 = c1.create_line(x0, y0, x1, y1)
            
        创建一个椭圆，填充 pink 色：  填充的参数 --- fill="pink"
            oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  #创建一个圆，填充色为`red`红色，两个x 值相等和两个y 值相等就是圆形了
            
        创建扇形：
            arc = c1.create_arc(x0+30, y0+30, x1+30, y1+30,start=0,extent=180) #  创建一个180° 的伞形
        矩形：
            rect = c1.create_rectangle(100,30,100+10,30+10) # 矩形
            
         画布中的子部件：前两个参数都是相对于画布的位置

"""
import tkinter as tk

# 窗口主题框架：
w = tk.Tk()
w.title("画布 Canvas")
w.geometry("600x600+300+50")

def moveit():
    # c1.move(rect, 0, 3)
    # c1.move(image, 0, 3)
    c1.move(oval, 0, 3)

# canvas 画布
c1 = tk.Canvas(w, bg="blue", height=200,width=400)
# 图片部件
image_file= tk.PhotoImage(file="ins.gif")
image = c1.create_image(10,10,anchor='nw',image=image_file)
# c1.create_image(10,10,anchor='nw',image=image_file)   也可行

x0, y0, x1, y1 = 50, 50, 80, 80
line1 = c1.create_line(x0, y0, x1, y1)  # 这段代码主要实现的是画一条直线，后面()中给的参数就是线段两点的坐标，两点确定一条直线。此处给的就是从坐标(50,50)到(80,80)画一条直线。

oval = c1.create_oval(x0, y0, x1, y1, fill="pink") # 椭圆
arc = c1.create_arc(x0+30, y0+30, x1+30, y1+30,start=0,extent=180) #  创建一个180° 的伞形
rect = c1.create_rectangle(100,30,100+10,30+10) # 矩形
c1.pack()

# 按钮button
b = tk.Button(w,text='move', width=15, height=2,command=moveit)
b.pack()



w.mainloop()
