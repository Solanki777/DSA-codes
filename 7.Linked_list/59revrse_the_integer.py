def rever(x):
    a=abs(x)
    s=0
    while a>0:
        d=a%10
        a=a//10
        s=s*10+d

    if x<0:
        s=-s

    if -2**31<=s and s<=2**31-1:
        return s
    return 0

print(rever(123))