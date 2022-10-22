import quanlyhocvien

student = quanlyhocvien.Quanlyhocvien()

while (True):
    print("------------------------------------")
    print("| Chuong trinh quan ly hoc vien-----|")
    print("| 1. Them hoc vien------------------|")
    print("| 2. Hien thi hoc vien--------------|")
    print("| 3. Sua thong tin hoc vien---------|")
    print("| 4. Xoa hoc vien-------------------|")
    print("| 5. Tim kiem hoc vien--------------|")
    print("| 6. Sap xep hoc vien---------------|")
    print("------------------------------------")

    nhap = int(input("Nhap chuc nang muon su dung: "))
    if (nhap == 1):
        n = int(input("Nhap so hoc vien muon them: "))
        j = 1
        while (j <= n):
            print("Nhap hoc vien thu {}".format(j))
            student.themhocvien()
            j+=1
            print("Da them xong 1 hoc vien")
        student.hienthihocvien()
    elif (nhap == 2):
        student.hienthihocvien()
    elif (nhap == 3):
        idsua = int(input("Nhap id hoc vien muon sua: "))
        student.suatthocvien(idsua)
        print("Da sua thong tin hoc vien")
        student.hienthihocvien()
    elif (nhap == 4):
        idxoa = int(input("Nhap id hoc vien muon xoa: "))
        student.xoahocvientheoid(idxoa)
        print("Da xoa hoc vien")
        student.hienthihocvien()
    elif (nhap==5):
        nametimkiem = input("Nhap ten muon tim")
        student.timkiemhocvien(nametimkiem)
    elif (nhap==6):
        student.sapxephocvien()
        student.hienthihocvien()
    elif (nhap == 0):
        print("Tam biet")
        break
    else:
        print("Chon sai vui long chon lai")

