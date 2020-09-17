from tkinter import *
from tkinter import ttk
def hello():
    print("hello")
    str=T.get(1.0,END) #row=1,column=0 in 1.0
    print(str)
def func():
    l2.configure(text=cb.get())

root=Tk()
root.geometry('200x100')
'''menubar = Menu()
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=hello)
filemenu.add_command(label='Open',command=hello)
filemenu.add_command(label='Save',command=hello)
filemenu.add_command(label='Save as...',command=hello)
filemenu.add_command(label='Close',command=hello)
filemenu.add_command(label='Exit',command=root.quit)
root.config(menu=menubar)
S = Scrollbar(root)
T = Text(root, height=4, width=50)
S.pack(side=RIGHT,fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.pack(side=LEFT,fill=Y)
str="""lfsadkl
sksmd
fal
dkf
"""
T.insert(END,str)
'''
l1=Label(root,text="choose lang")
l1.grid(row=0,column=0)
course=("Java","Python","C++")
cb=ttk.Combobox(root,values=course,width=10,state='readonly')
cb.grid(row=1,column=0)
cb.current(0)
b=Button(root,text="click here",command=func)
b.grid(row=2,column=0)
l2=Label(root,text="")
l2.grid(row=3,column=0)
root.mainloop()

