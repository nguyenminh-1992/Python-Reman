from reman import PythonReman
# C R U D
class Quanlyhocvien:

    listhocvien = []

    def themhocvien(self):
        id = int(input("Nhap id: "))
        name = input("Nhap ten: ")
        age = int(input("Nhap tuoi: "))
        country = input("Nhap que quan: ")
        diemtin = float(input("Nhap diem tin: "))
        diemtienganh = float(input("Nhap diem tieng anh: "))
        self.listhocvien.append(PythonReman(id,name,age,country,diemtin,diemtienganh))
    
    def hienthihocvien(self):
        for i in self.listhocvien:
            print(i.id,i.name,i.age,i.country,i.diemtin,i.diemtienganh,sep=" - ")

    # def xoahocvien(self):


    # def suatthocvien(self):


