import tkinter

giaodien = tkinter.Tk()
giaodien.title("Tinh tong hai so nguyen")
giaodien.geometry('500x400')

label1 = tkinter.Label(giaodien,text="Tính tổng hai số nguyên",fg="black",bg="white")
label1.grid(column=2,row=0)

label2 = tkinter.Label(giaodien,text="Nhap so thu nhat",fg="black",bg="white")
label2.grid(column=0,row=1)

label3 = tkinter.Label(giaodien,text="Nhap so thu hai",fg="black",bg="white")
label3.grid(column=0,row=2)

label4 = tkinter.Label(giaodien,text="Ket qua: ",fg="black",bg="white")
label4.grid(column=0,row=3)

textbox1 = tkinter.Entry(giaodien,width=30)
textbox1.grid(column=2,row=1)

textbox2 = tkinter.Entry(giaodien,width=30)
textbox2.grid(column=2,row=2)

textbox3 = tkinter.Entry(giaodien,width=30)
textbox3.grid(column=2,row=3)

button = tkinter.Button(giaodien,text="Ket qua",bg="blue",fg="black")
button.grid(column=1,row=4)


giaodien.mainloop()