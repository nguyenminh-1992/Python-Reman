import quanlyhocvien

student = quanlyhocvien.Quanlyhocvien()

while (True):
    print("------------------------------------")
    print("| Chuong trinh quan ly hoc vien-----|")
    print("| 1. Them hoc vien------------------|")
    print("| 2. Hien thi hoc vien--------------|")
    print("| 3. Sua thong tin hoc vien---------|")
    print("| 4. Xoa hoc vien-------------------|")
    print("------------------------------------")

    nhap = int(input("Nhap chuc nang muon su dung: "))
    if (nhap == 1):
        n = int(input("Nhap so hoc vien muon them: "))
        j = 1
        while (j <= n):
            student.themhocvien()
            j+=1
            print("Da them xong 1 hoc vien")
        student.hienthihocvien()
    elif (nhap == 2):
        student.hienthihocvien()
    elif (nhap == 3):
        print("Chuc nang sua thong tin hoc vien") 
    elif (nhap == 4):
        print("Chuc nang xoa hoc vien") 
    elif (nhap == 0):
        print("Tam biet")
        break
    else:
        print("Chon sai vui long chon lai")

