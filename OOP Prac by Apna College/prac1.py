# Create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average

class Student:
    def __init__(self , name , maths , english , science):
        self.name = name
        self.maths = maths
        self.english = english
        self.science = science
    
    def average(self):
        avg = (self.maths + self.english +self.science) //3
        return avg


s1 = Student("John",90 ,67, 89)
print(s1.average())

s2 = Student("Alice",87 , 98 , 70)
print(s2.average())

s3 = Student("Mark",94 , 92 , 95)
print(s3.average())

