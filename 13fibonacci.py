# fibonacci is a series where it is like 0,1,1,2,3,5,8,13,21,34 means here increament of one number and sumation with previous number.

# first we doing this using simple method
# a=0
# b=1
# n=int(input("enter a number of series"))
# print(a," ")
# print(b," ")
# for i in range(n-2):
#     c=a+b
#     a=b
#     b=c
#     print(c)

# using recursion
# def feb(a,b,i,n):
#     if i==n-2:
#         return
#     if i==0:
#         print(a)
#         print(b)
#     c=a+b
#     print(c)
#     feb(b,c,i+1,n)
        
# feb(0,1,0,5)

# now we are finding the fibonnaci answer for particular number like for
# 0 1 2 3 4 5 -index
# 0 1 1 2 3 5 -fibonnaci
# now index is given find fibonnaci number 

def feb(n):
    if n==0 or n==1:
        return n
    return feb(n-1)+feb(n-2)


n=int(input("enter a number:"))
ans=feb(n)
print(ans)

# here in above case for any element n it will call 2 types for n-1 ans n-2 so the time complexity is O(2^n) where 2 is for 2 calls and n for n element and stack space or space compleity is also 2 ^n because every time stack space is created for both calls for n types


