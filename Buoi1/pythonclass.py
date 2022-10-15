#Var
#Array (List, Tuple, Set, Dic)
# Person1 = {}
# Person2 = 
#Function
#Class
#O O P: Object Oriented Programming (Lap trinh huong doi tuong)

class Person():
    name = 'abc'
    age = 0
    country = 'HN'
    def __init__(self,name='abc',age = 0,country= 'HN'): # Dinh nghia
        self.name = name
        self.age = age
        self.country = country
    #Thuoc tinh
    def eat(self):
        print("An ngay du 3 bua")
    def sleep(self):
        print("Ngu 8 tieng moi ngay")
    def play(self):
        print("Choi the thao 2 tieng moi ngay")

person1 = Person("Minh",20,"Ha Noi")
# person2 = Person("Tuan",21,"Hue")
# person3 = Person("Quang",22,"HCM")

# person1.eat()
# person2.sleep()
# print(person1.name)
# print(person2.age)

# person1 = Person()
person2 = Person()
print(person1.name)
print(person2.name)