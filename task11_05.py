class Dog:
    def __init__(self, name):
        self.name = name
    def change_name(self):
        new_name = input("Введите имя песику: \n")
        self.name= new_name

dog = Dog("Bobik")

print(dog.name)
dog.change_name()
print(dog.name)