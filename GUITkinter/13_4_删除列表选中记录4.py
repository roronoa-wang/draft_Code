from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox

class Application(Frame) :
    def selected(self):
        curItem = self.tree.focus()
        print(self.tree.item(curItem)['values'][0])
        self.quit()

    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.grid()

        tree = self.tree = Treeview(self,columns=('Name','Description'),show="headings",selectmode='browse')
        tree.heading("Name", text="Name")
        tree.heading("Description", text="Description")
        tree.grid(padx = 30)

        i = tree.insert('','end',values = ['0353','567'])
        tree.insert(i,'end',values = ['03535','567'])
        Button(self,text = "Submit",command = self.selected).grid()

        # i = tree.insert('','end',values = ['0353','567'])
        # tree.insert(i,'end',values = ['03535','567'])
        # Button(self,text = "Submit",command = self.selected).grid()


root = Tk()
app = Application()
app.master.title("Tree view")
app.master.minsize(500, 400)
app.master.protocol(name = "WM_DELETE_WINDOW",func=app.master.quit)

app.mainloop()
root.destroy()