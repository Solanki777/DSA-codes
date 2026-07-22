
# it is used when some function is dependent on some value and it's repadily changed so we use property there to calculate . But it used in python's olded version like 2.2 in new one it changed and fix it so we not have to use property  
class Student:
    def __init__(self,name ,m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @property    
    def cal_pr(self):
        pr = str((self.m1 + self.m2 + self.m3) // 3 )+ "%"
        return pr 

s1 = Student("John" , 87 ,75 ,98)
print(s1.cal_pr())

# Now there is mistack in marks
s1.m1 = 78
print(s1.cal_pr())
