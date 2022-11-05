import connectsql

ketnoi = connectsql.getConnection()
# print(ketnoi)
#C R U D
# SELECT * FROM Quan_ly_hoc_vien.Hocvien;

#Get data
dulieu = ketnoi.cursor()

def getalldata():
   dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
   ketqua = dulieu.fetchall()
   for i in ketqua:
    print(i)

def getalldata2():
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
    ketqua = dulieu.fetchone()
    while ketqua is not None:
        print(ketqua)
        ketqua = dulieu.fetchone()



# getalldata()
getalldata2()


ketnoi.close()