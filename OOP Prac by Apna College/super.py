

# Super only worked with method not instance varibles
class College:
    def __init__(self,college_name):
        self.college_name = college_name

class Student(College):
    def __init__(self,c_name,name):
        self.name = name
        super().__init__(c_name)


s1 = Student("SSEC","Mahesh")
print(s1.name)
print(s1.college_name)



# How to access class varibales

# 1. normal way 
class Person:
    name = "annonymous"
    def __init__(self,name):
        # 1.# Person.name = name
        #2
        self.__class__.name = name


print(Person.name)
Person("John")
print(Person.name)


# using class decorator
class Person:
    name = "annonymous"

    @classmethod
    def __init__(cls,name):
        cls.name = name

Person("Lanna")
print(Person.name)        