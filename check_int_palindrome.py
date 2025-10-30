n=12121
result=0
num=n

while(num>0):
    id=num%10 #it finds last digit
    result=(result*10)+id #it makes reverse string of num by taking last element multiplying with 10 to increase order and by adding the bits

    num=num//10 #it reduces the size of digit by one

print("palindrome",result==n)

