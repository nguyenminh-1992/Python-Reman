from reman import PythonReman
# C R U D
# Them, Xem, Sua, Xoa


class Quanlyhocvien:

    listhocvien = []
    # def __init__(self):
    #     self.themhocvien()
    #     self.hienthihocvien()

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

# if __name__ == "__main__":
#     Quanlyhocvien()

#Test
student1 = Quanlyhocvien()
student1.themhocvien()
student1.hienthihocvien()

