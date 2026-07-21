class Car:
    def __init__(self , name , milage , price):
        self.name = name
        self.milage = milage
        self.price = price

c1 = Car("toyota" , 50 , 55000) # all values are wrapped in one object is called encapsualtion
print(c1.name)
        