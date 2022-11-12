# G U I

# pip3 install tkinter
import tkinter
from tkinter.ttk import Combobox
from tkinter import Checkbutton, Radiobutton, IntVar, Spinbox
from tkinter.scrolledtext import ScrolledText


#Tao khung giao dien
giaodien = tkinter.Tk()
giaodien.title("Demo GUI")
giaodien.geometry('500x400')

#Label
label = tkinter.Label(giaodien,text="Xin chao den voi chuong trinh",fg="black",bg="white")
label.grid(column=2,row=0)

#Textbox
textbox = tkinter.Entry(giaodien,width=30)
textbox.grid(column=2,row=1)

#Button
button = tkinter.Button(giaodien,text="Click me",bg="blue",fg="black")
button.grid(column=2,row=2)

#Combobox
combobox = Combobox(giaodien)
combobox['values'] = (1,2,3,4,'Text')
combobox.grid(column=2,row=3)

#Checkbox
checkbox1 = Checkbutton(giaodien,text="Lua chon 1")
checkbox1.grid(column=2,row=4)

checkbox2 = Checkbutton(giaodien,text="Lua chon 2")
checkbox2.grid(column=2,row=5)

#Radiobox
select = IntVar()
radiobox1 = Radiobutton(giaodien, text="Choose 1",variable=select)
radiobox1.grid(column=2,row=6)

select = IntVar()
radiobox2 = Radiobutton(giaodien, text="Choose 2",variable=select)
radiobox2.grid(column=2,row=7)

#Scrolled Text
scrolled = ScrolledText(giaodien,width=20,height = 10)
scrolled.grid(column=2,row=8)

#Spinbox
spinbox = Spinbox(giaodien,from_=1,to=10,width=10)
spinbox.grid(column=2,row=9)



giaodien.mainloop()