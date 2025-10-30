# if 153=1^3+5^3+3^3
#       =153
# so this is how the armstrong number is

# time complexity =0(logbase10 N)
num=1634
s=0
m=num

while(m>0):

    m=num%10
    s+=m*m*m*m

    num=num//10



print(s)
