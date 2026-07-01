# head recursion:
# print number n times using recurison
# def func(c,n):
#     if c==0:
#         return
#     print(n)
#     func(c-1,n)

# func(4,15)

# print 1 to N using recursion

# def func(n,i):
#     if n<i:
#         return
#     print(i)
#     func(n,i+1)


# func(10,1)

# tail recurision

def ani(i,n):
    if i<n:
        return
    ani(i-1,n)
    print(i)
ani(10,1)