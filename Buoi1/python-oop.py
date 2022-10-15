class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sleep(self):
        print("Person sleep")
    def sport(slef):
        print("Person running")

class BKACAD():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self):
        print("BKACAD study")
    def exam(self):
        print("Exam")
# Ke thua
class Reman1(BKACAD,Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
   

class Reman2(BKACAD):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    
student1 = Reman1('Quang',20)
student2 = Reman2('Vinh',30)

student1.study()
student2.study()
student1.sleep()