import tkinter
#Tao phan giao dien
giaodien = tkinter.Tk()
giaodien.title("Tinh tong hai so nguyen")
giaodien.geometry('500x200')

label1 = tkinter.Label(giaodien,text="Tính tổng hai số nguyên",fg="black",bg="white")
label1.grid(column=2,row=0)

label2 = tkinter.Label(giaodien,text="Nhap so thu nhat",fg="black",bg="white")
label2.grid(column=0,row=1)

label3 = tkinter.Label(giaodien,text="Nhap so thu hai",fg="black",bg="white")
label3.grid(column=0,row=2)

label4 = tkinter.Label(giaodien,text="Ket qua: ",fg="black",bg="white")
label4.grid(column=0,row=3)

#Phan de lam viec
dulieu1 = tkinter.IntVar()
textbox1 = tkinter.Entry(giaodien,width=30,textvariable=dulieu1)
textbox1.grid(column=2,row=1)
textbox1.focus()

dulieu2 = tkinter.IntVar()
textbox2 = tkinter.Entry(giaodien,width=30,textvariable=dulieu2)
textbox2.grid(column=2,row=2)
textbox2.focus()

dulieu3 = tkinter.IntVar()
textbox3 = tkinter.Entry(giaodien,width=30,textvariable=dulieu3)
textbox3.grid(column=2,row=3)
textbox3.focus()

# def sukien():
#     tong = int(dulieu1.get()) + int(dulieu2.get())
#     dulieu3.set(tong)
#     dulieu1.set("")
#     dulieu2.set("")

# button = tkinter.Button(giaodien,text="Ket qua",bg="blue",fg="black",command= sukien)
# button.grid(column=1,row=4)

def cong():
    tong = int(dulieu1.get()) + int(dulieu2.get())
    dulieu3.set(tong)
    dulieu1.set("")
    dulieu2.set("")

def tru():
    hieu = int(dulieu1.get()) - int(dulieu2.get())
    dulieu3.set(hieu)
    dulieu1.set("")
    dulieu2.set("")

def nhan():
    tich = int(dulieu1.get()) * int(dulieu2.get())
    dulieu3.set(tich )
    dulieu1.set("")
    dulieu2.set("")

def chia():
    thuong = int(dulieu1.get()) / int(dulieu2.get())
    dulieu3.set(thuong)
    dulieu1.set("")
    dulieu2.set("")

button = tkinter.Button(giaodien,text="+",bg="blue",fg="black",command= cong)
button.grid(column=0,row=4)

button = tkinter.Button(giaodien,text="-",bg="blue",fg="black",command= tru)
button.grid(column=1,row=4)

button = tkinter.Button(giaodien,text="x",bg="blue",fg="black",command= nhan)
button.grid(column=0,row=5)

button = tkinter.Button(giaodien,text=":",bg="blue",fg="black",command= chia)
button.grid(column=1,row=5)


giaodien.mainloop()