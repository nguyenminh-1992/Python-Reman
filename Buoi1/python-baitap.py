#Viết chương trình nhập thông tin lớp Python
#Bước 1: Nhấp số học viên
#Bước 2: Điền thông tin mỗi học viên (tên, tuổi, quê quán)
#Bước 3: Hiển thị danh sách lớp Python

#Ví dụ: 
#B1: 3 -> 3 học viên
#B2: Nhập 
#B3: Nguyen Van A - 20 - Ha Noi
# Nguyen Van B - 21 - HCM
# Nguyen Van C - 22 - Hue

#Tạo Class Python, định nghĩa các thông tin ở __init__
#Khai bao 1 List 
#In ra theo For
# student1, student2, student3
# A = [student1, student2, student3]
#student1.name, student1.age, student1.country

#C R U D
# Create
# Read
# Update
# Delete

#Dinh nghia: Ten, tuoi, que quan
#Create - Read

class PythonReman:
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country
#Giong nhau -> For, While
name1 = input("Nhap ten: ")
age1 = int(input("Nhap tuoi: "))
country1 = input("Nhap que quan: ")

student1 = PythonReman(name1,age1,country1)

n = int(input("Nhap sp luong hoc vien: "))


