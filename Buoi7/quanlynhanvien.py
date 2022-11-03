# C R U D
from nhanvien import Nhanvien


class Quanlynhanvien:

    listnhanvien = []

    def themhocvien(self):
        # id = int(input("Nhap id: "))
        name = input("Nhap ten: ")
        age = int(input("Nhap tuoi: "))
        country = input("Nhap que quan: ")
        
        sex = int(input("Nhap gioi tinh (0:Unknown, 1:Male, 2:Female): "))
        if (sex == 0):
            sex = "Unknown"
        elif (sex == 1): 
            sex = "Male"
        elif (sex == 2):
            sex = "Female" 
        else:
            print("Vui long nhap lai")     
        
        chucvu = input("Nhap chuc vu: ")
        if (chucvu == "GD"):
            chucvu1 = "Giam doc"
        elif (chucvu == "TP"):
            chucvu1 = "Truong phong"
        elif (chucvu == "CB"):
            chucvu1 = "Can bo"
        else:
            print("Nhap sai")
        
        n = 1
        id = chucvu + str(n)
        for i in self.listnhanvien:
            if (i.id == id):
                n += 1
                id = chucvu + str(n)
        
        chamcong = int(input("Nhap so ngay cong: "))
        nhanvien = Nhanvien(id,name,age,country,sex,chucvu1,chamcong)
     
        if (chucvu == "GD"):
            nhanvien.luong = chamcong * 1000000
        elif (chucvu == "TP"):
            nhanvien.luong = chamcong * 500000
        else:
            nhanvien.luong = chamcong * 400000

        self.listnhanvien.append(nhanvien)

    def hienthinhanvien(self):
        print("{:<8} {:<15} {:<8} {:<12} {:<15} {:<15} {:<15} {:<15}".format("Id","Ten","Tuoi","Que quan","Gioi tinh","Chuc vu","Cham cong","Luong"))
        for i in self.listnhanvien:
            print("{:<8} {:<15} {:<8} {:<12} {:<15} {:<15} {:<15}  {:<15}".format(i.id,i.name,i.age,i.country,i.sex,i.chucvu,i.chamcong,i.luong,sep=" - "))


