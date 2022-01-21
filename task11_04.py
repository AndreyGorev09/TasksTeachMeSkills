class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
    def jump(self):
        print("Jump!")
    def run(self):
        print("Run!")
    def bark(self):
        print("Gav Gav!")
dog = Dog(40, 20, "Bobik", 4)

dog.jump()
dog.run()
dog.bark()
print(dog.height, dog.weight, dog.name, dog.age)
