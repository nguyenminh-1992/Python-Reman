import quanlynhanvien

nhanvien = quanlynhanvien.Quanlynhanvien()

while (True):
    print("------------------------------------")
    print("| Chuong trinh quan ly nhan vien-----|")
    print("| 1. Them nhan vien------------------|")
    print("| 2. Hien thi nhan vien--------------|")
    print("| 3. Sua thong tin nhan vien---------|")
    print("| 4. Xoa nhan vien-------------------|")
    print("| 5. Tim kiem nhan vien--------------|")
    print("| 6. Sap xep nhan vien---------------|")
    print("------------------------------------")

    nhap = int(input("Nhap chuc nang muon su dung: "))
    if (nhap == 1):
        n = int(input("Nhap so nhan vien muon them: "))
        j = 1
        while (j <= n):
            print("Nhap hoc vien thu {}".format(j))
            nhanvien.themhocvien()
            j+=1
            print("Da them xong 1 hoc vien")
        nhanvien.hienthinhanvien()
    elif (nhap == 2):
        nhanvien.hienthinhanvien()
    elif (nhap == 3):
         print("")
    elif (nhap == 4):
         print("")
    elif (nhap==5):
         print("")
    elif (nhap==6):
        print("")
    elif (nhap == 0):
        print("Tam biet")
        break
    else:
        print("Chon sai vui long chon lai")

