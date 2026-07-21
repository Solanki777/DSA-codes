# Create account class with 2 attributes - balance and acccount no. create methods for debit , credit and printing the balance

class Bank:
    def __init__(self , acc_no , bal ):
        self.acc_no = acc_no
        self.bal = bal
    
    def credit(self , amount):
        self.bal += amount
        print(f"you account {self.acc_no} has credited {amount} and now you balance is {self.bal} ")

    def debit(self,amount):
        if amount > self.bal:
            print("insufficient balance") 
        else:
            self.bal -= amount
            print(f"your account {self.acc_no} has debited {amount} and now you balance is {self.bal}")
    
    def check_bal(self):
        print(f"Your account has {self.bal}")
a1 = Bank(1 , 100)
a1.credit(100)
a1.credit(500)
a1.credit(100)
a1.debit(800)
a1.debit(200)
a1.check_bal()

a2 = Bank(2 , 500)
a2.credit(489500)
a2.credit(5265400)
a2.credit(145600)
a2.debit(4589999800)
a2.debit(2598400)
a2.check_bal()