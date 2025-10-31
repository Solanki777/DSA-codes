# factors like for 10 =[1,2,5,10]
#                   11 =[1,11]

num=int(input("enter a number:"))
i=1
divisior=[]
while (i<=num):
        if num%i==0:
                divisior.append(i)
        i+=1

print(divisior)
                
        