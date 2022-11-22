#Buoc 1: Tao giao dien

import tkinter
from tkinter.scrolledtext import ScrolledText
import connectsql
from tkinter import END

giaodien = tkinter.Tk()
giaodien.title("Chuong trinh quan ly hoc vien")
giaodien.geometry("450x500")


#Buoc 2: Xay dung chuc nang

connection = connectsql.getConnection()
dulieu = connection.cursor()

def kiemtraketnoi():
    if(connection.is_connected):
        label2.config(text= "Ket noi thanh cong")
    else:
        label2.config(text= "Ket noi khong thanh cong")

def hienthihocvien():
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
    ketqua = dulieu.fetchall()
    scrolled.configure(state="normal")
    scrolled.delete("1.0", END)
    for i in ketqua:
        ketqua = str(i) + ","
        scrolled.configure(state="normal")
        scrolled.insert(tkinter.INSERT, ketqua + "\n")
        scrolled.configure(state = "disable")
    return ketqua
    

label1 = tkinter.Label(giaodien, text = "CHUONG TRINH QUAN LY HOC VIEN",fg="black",font=("Arial Bold", 10))
label1.grid(column=1,row=1)

label2 = tkinter.Label(giaodien, text = "",fg="black",font=("Arial Bold", 10))
label2.grid(column=1,row=4)

button1 = tkinter.Button(giaodien, text ="Kiem tra ket noi", fg="black",bg="white",command= kiemtraketnoi)
button1.grid(column=1,row=3)

button2 = tkinter.Button(giaodien, text ="Hien thi hoc vien", fg="black",bg="white",command = hienthihocvien)
button2.grid(column=1,row=5)

scrolled = ScrolledText(giaodien, width = 60,height = 10, state = "disable")
scrolled.grid(column=1,row=6)



giaodien.mainloop()