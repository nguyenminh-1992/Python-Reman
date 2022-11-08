import quanlyhocvien

# quanlyhocvien.getdatabyid2(1)
# quanlyhocvien.createdata()
while(True):
    print("1. Get all data")
    print("2. Get data by ID")
    print("3. Create data")
    print("4. Update data")
    print("5. Delete data")

    nhap=int(input("Chon chuc nang: "))
    if(nhap==1):
        hienthi = quanlyhocvien.getalldata()
        print(hienthi)
    if(nhap==2):
        id = int(input("Nhap id: "))
        hienthi = quanlyhocvien.getdatabyid2(id)
        print(hienthi)
    elif(nhap==0):
        print("Bye")
        break
    else:
        print("Nhap sai vui long nhap lai")

