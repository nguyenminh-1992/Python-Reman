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

def getdatabyid():
    dulieu.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = 3")
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)

def getdatabyid2(id):
    sql = "SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = %s"
    # id = 3
    dulieu.execute(sql,(id,))
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)
    
def getdatabyidandage(id,age):
    sql = "SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = %s And age = %s"
    # id = 3
    dulieu.execute(sql,(id,age))
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)


# SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = 2 OR Age = 21;

# getalldata()
# getalldata2()
# getdatabyid()
getdatabyid2(1)


ketnoi.close()