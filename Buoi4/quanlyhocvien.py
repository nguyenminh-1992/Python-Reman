from reman import PythonReman
# C R U D
# Them, Xem, Sua, Xoa


class Quanlyhocvien:

    listhocvien = []
    # def __init__(self):
    #     self.themhocvien()
    #     self.hienthihocvien()

    def themhocvien(self):
        id = self.listhocvien.__len__() + 1
        name = input("Nhap ten: ")
        age = int(input("Nhap tuoi: "))
        country = input("Nhap que quan: ")
        diemtin = float(input("Nhap diem tin: "))
        diemtienganh = float(input("Nhap diem tieng anh: "))
        diemtrungbinh = float((diemtin + diemtienganh)/2)
        hocvien = PythonReman(id,name,age,country,diemtin,diemtienganh)
        if diemtrungbinh > 5:
            hocvien.hocluc = "Gioi"
        else:
            hocvien.hocluc = "Trung binh"
         #   (id,name,age,country,diemtin,diemtienganh,hocluc)
        # self.listhocvien.append(PythonReman(id,name,age,country,diemtin,diemtienganh))
        self.listhocvien.append(hocvien) #PythonReman + hocluc
        
        
#Id tu dong tang
#Diemtrungbinh = (tin + tieng anh) /2
#Hocluc: >5: Gioi, <5: Trungbinh
    
    def hienthihocvien(self):
        for i in self.listhocvien:
            print(i.id,i.name,i.age,i.country,i.diemtin,i.diemtienganh,i.hocluc,sep=" - ")
    
    def xoahocvientheoid(self,id):
        for i in self.listhocvien:
            if(i.id == id):
                self.listhocvien.remove(i)
    
    def suatthocvien(self,idcantim):  #Sua theo ten va tuoi
        for i in self.listhocvien:
            if(i.id == idcantim):
                i.name = input("Nhap ten: ")
                i.age = int(input("Nhap tuoi: "))

    def timkiemhocvien(self,nametimkiem): 
        for i in self.listhocvien:
            if(i.name == nametimkiem):
                print("Da tim thay")  
                print(i.id,i.name,i.age,i.country,i.diemtin,i.diemtienganh,sep=" - ") 
            else:
                print("Khong thay nguoi can tim")

# if __name__ == "__main__":
#     Quanlyhocvien()

#Test
# student1 = Quanlyhocvien()
# student1.themhocvien()
# student1.hienthihocvien()

