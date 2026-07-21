

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



