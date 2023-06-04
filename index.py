from tkinter import Tk, messagebox, END, E, W, Label, Entry, Button
from windnd import hook_dropfiles
from os import path, symlink


def on_drop(event, index):
    print(event)
    entry = entry1 if index == 0 else entry2
    entry.delete(0, END)
    entry.insert(0, event[0])
    # event.widget.delete(0, END)
    # event.widget.insert(0, event.data)


root = Tk()
root.title("创建符号链接")

Label(root, text="源路径").grid()
entry1 = Entry(root)
entry1.grid(row=0, column=1, sticky=E + W)
hook_dropfiles(entry1, lambda x: on_drop(x, 0), True)

Label(root, text="目标路径").grid(row=1)
entry2 = Entry(root)
entry2.grid(row=1, column=1, sticky=E + W)
hook_dropfiles(entry2, lambda x: on_drop(x, 1), True)

Label(root, text="可将文件拖入输入框").grid(row=2, columnspan=2, sticky=W)


def createLink():
    if not path.exists(entry1.get()):
        messagebox.showerror(None, "源路径不存在")
        return
    if path.exists(entry2.get()):
        messagebox.showerror(None, "目标路径已存在")
        return
    symlink(entry1.get(), entry2.get(), path.isdir(entry1.get()))


btn = Button(root, text="创建", command=createLink).grid(row=3, columnspan=2)

root.columnconfigure(1, weight=1)
root.mainloop()
