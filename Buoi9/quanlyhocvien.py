import connectsql

ketnoi = connectsql.getConnection()
# print(ketnoi)
#C R U D
# SELECT * FROM Quan_ly_hoc_vien.Hocvien;

#Get data
dulieu = ketnoi.cursor()

def getalldata():
    diemTB = []
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
    ketqua = dulieu.fetchall()
    for diem in ketqua:
        i,j = diem[-2:]
        dtb = (i+j)/2
        if dtb>=7.5:
            dt = list(diem) + [dtb] + ['Gioi']
        elif 5<=dtb<=7:
            dt = list(diem) + [dtb] + ['Trung binh']
        else:
            dt = list(diem) + [dtb] + ['Yeu']
        diemTB.append(tuple(dt))
    
    for i in diemTB:
        print(i)
    # ketnoi.close()

def getalldata2():
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
    ketqua = dulieu.fetchone()
    while ketqua is not None:
        print(ketqua)
        ketqua = dulieu.fetchone()
    ketnoi.close()

def getdatabyid():
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = 3")
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)
    # ketnoi.close()

def getdatabyid2(id):
    sql = "SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = %s"
    # id = 3
    dulieu.execute(sql,(id,))
    ketqua = dulieu.fetchall()
    for i in ketqua:
        return i
    # ketnoi.close()
    
def getdatabyidandage(id,age):
    sql = "SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = %s And age = %s"
    # id = 3
    dulieu.execute(sql,(id,age))
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)
    # ketnoi.close()

def createdata():
    sql = "INSERT INTO Quan_ly_hoc_vien.`Hocvien`(Id,`Name`,Age, Country,English,Information) VALUES (7,'Nguyen Van G',29,'Nha Trang',7,6)"
    dulieu.execute(sql)
    ketnoi.commit()
    print("Da them thanh cong")
    # ketnoi.close()

def updatedata():
    sql = "UPDATE Quan_ly_hoc_vien.Hocvien SET Age = 26 WHERE Id = 6"
    dulieu.execute(sql)
    ketnoi.commit()
    print("Da update thanh cong")
    # ketnoi.close()

def deletedata():
    sql = "DELETE FROM Quan_ly_hoc_vien.Hocvien WHERE Country = 'Nha Trang'"
    dulieu.execute(sql)
    ketnoi.commit()
    print("Da xoa du lieu")
    # ketnoi.close()


# SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = 2 OR Age = 21;

# getalldata()
# getalldata2()
# getdatabyid()
# getdatabyid2(1)
# createdata()
# updatedata()
# deletedata()



# ketnoi.close()
