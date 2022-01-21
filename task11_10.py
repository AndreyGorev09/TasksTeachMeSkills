class Pet:
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
    def __init__(self,sound,height,weight,name,age,master):
        self.sound = sound
        super().__init__(height,weight,name,age,master)
class Cat(Pet):
    def __init__(self, sound,height, weight, name, age, master):
        self.sound = sound
        super().__init__(height, weight, name, age, master)
class Parrot(Pet):
    def __init__(self,sound,height, weight, name, age, master):
        self.sound = sound
        super().__init__(height, weight, name, age, master)

a = Dog("Gav", 45, 15, "Dig", 3, "Andrei")
b = Cat("Mau", 25, 5, "Gir", 2, "Lisa")
c = Parrot("Chik-chik", 10, 0.2, "Rikki", 4, "Danil")
print(a.__dict__)
print(b.__dict__)
print(c.__dict__)
