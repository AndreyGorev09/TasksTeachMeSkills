class Pes:
    def __init__(self, height, weight, name, age, master):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age
        self.__master = master

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def master(self):
        return self.__master
    @master.setter
    def master(self, master):
        self.__master = master

class Dog(Pet):
    def sound(self):
        return "Gav"
class Cat(Pet):
    def sound(self):
        return "Mau"
class Parrot(Pet):
    def sound(self):
        return 'Chik chirik'
print(Dog.mro())

