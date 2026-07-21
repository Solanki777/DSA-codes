class Car:
    def __init__(self , name):
        self.name = name

c1 = Car("Lambo")
print(c1.name)
del c1
print(c1)