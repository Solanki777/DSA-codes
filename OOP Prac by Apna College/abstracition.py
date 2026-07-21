class Car:
    def __init__(self):
        self.brk = False
        self.cluth = False
        self.acc = False
    
    def start(self):
        self.brk = False
        self.cluth =True
        self.acc =True
        print('car started ...')

c1 = Car()
# c1.start() we know is just car started not how internal workes this is abstraction