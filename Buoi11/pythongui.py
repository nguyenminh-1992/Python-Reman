# G U I

# pip3 install tkinter
import tkinter
from tkinter.ttk import Combobox


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




giaodien.mainloop()