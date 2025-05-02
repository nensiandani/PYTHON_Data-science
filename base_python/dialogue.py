import tkinter as tk

from tkinter.colorchooser import askcolor
def callback():
    result=askcolor()
    print(result)

root=tk.Tk()
tk.Button(root,text='choose color',fg='darkgreen',command=callback).pack()
tk.mainloop()