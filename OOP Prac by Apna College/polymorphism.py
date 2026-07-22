
# print(2+3)  # summation
# print(type)
# print("Mashes" + "Solanki") # sting concate
# print(type("Mahesh")) 
# print([1,2,3] + [4,5,6])  # list merge
# print(type([1,2,3]))

# # as all diffrent type of class and the classes has diffrent mining of + so they worked like wise  this is called polymorphism : operator overloading


# # let's make a class that can sum two complex number 
# # there is no any functionality to add complex number 
# class Complex :
#     def __init__(self , real, img):
#         self.real = real
#         self.img = img
    
#     def show(self):
#         print(self.real ,"i +" , self.img,"j" )
    
#     def add(self,n2):
#         self.new_real = self.real + n2.real
#         self.new_img = self.img + n2.img
#         c3 = Complex(self.new_real , self.new_img)
#         return c3

# c1 = Complex(6,4)
# c1.show()
# c2 = Complex(2,3)
# c2.show()
# c3 = c2.add(c1)
# c3.show()

# but writing function is not sufficient i want to make like just do 
# c3 = c1 + c2
class Complex :
    def __init__(self , real, img):
        self.real = real
        self.img = img
    
    def show(self):
        print(self.real ,"i +" , self.img,"j" )
    
    def __add__(self,n2):
        self.new_real = self.real + n2.real
        self.new_img = self.img + n2.img
        c3 = Complex(self.new_real , self.new_img)
        return c3

c1 = Complex(6,4)
c1.show()
c2 = Complex(2,3)
c2.show()
# c3 = c1 + c2 it gives error now we use dunder function 
c3 = c1 + c2
print(c3.show())