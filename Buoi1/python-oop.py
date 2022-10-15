class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sleep(self):
        print("Person sleep")
    def sport(self):
        print("Person running")
    def eat(self):
        print("Person eat")

class BKACAD():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self):
        print("BKACAD study")
    def exam(self):
        print("Exam")
    def eat(self):
        print("BKACAD eat")
# Ke thua
class Reman1(BKACAD,Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def in_thong_tin(self):
        print("Hoc vien lop Reman1")
   

class Reman2(BKACAD):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def in_thong_tin(self):
        print("Hoc vien lop Reman2")

def kiemtra(sv):
    sv.in_thong_tin()

student1 = Reman1('Quang',20)
student2 = Reman2('Vinh',30)

student1.study()
student2.study()
student1.sleep()
student1.eat()

kiemtra(student1)
kiemtra(student2)