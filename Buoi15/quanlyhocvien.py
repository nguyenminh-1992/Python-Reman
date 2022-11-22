#Buoc 1: Tao giao dien

import tkinter
from tkinter.scrolledtext import ScrolledText

giaodien = tkinter.Tk()
giaodien.title("Chuong trinh quan ly hoc vien")
giaodien.geometry("450x500")

label1 = tkinter.Label(giaodien, text = "CHUONG TRINH QUAN LY HOC VIEN",fg="black",font=("Arial Bold", 10))
label1.grid(column=1,row=1)

label2 = tkinter.Label(giaodien, text = "",fg="black",font=("Arial Bold", 10))
label2.grid(column=1,row=4)

button1 = tkinter.Button(giaodien, text ="Kiem tra ket noi", fg="black",bg="white")
button1.grid(column=1,row=3)

button2 = tkinter.Button(giaodien, text ="Hien thi hoc vien", fg="black",bg="white")
button2.grid(column=1,row=5)

scrolled = ScrolledText(giaodien, width = 30,height = 10, state = "disable")
scrolled.grid(column=1,row=6)

#Buoc 2: Xay dung chuc nang

giaodien.mainloop()