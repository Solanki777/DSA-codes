class Bank:
    def __init__(self,ac_no,ac_pass):
        self.ac_no = ac_no
        self.ac_pass = ac_pass

b = Bank(1,"abc")
print(b.ac_no)
print(b.ac_pass) #pass is public so for security purpose we have to make it private





class Bank:
    def __init__(self,ac_no,ac_pass):
        self.ac_no = ac_no
        self.__ac_pass = ac_pass

b = Bank(1,"abc")
print(b.ac_no)
# print(b.__ac_pass) #NOw pass is safe




# how to access private things
class Bank:
    def __init__(self,ac_no,ac_pass):
        self.ac_no = ac_no
        self.__ac_pass = ac_pass
    
    def show_pass(self):
        return self.__ac_pass

b = Bank(1,"abc")
print(b.ac_no)
print(b.show_pass()) 