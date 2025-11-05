# Here we do some promblem like sum of 1 to N numbers using recursion
# mehtod used by code and debug

# parameterized recursions:where printitng is done within a function
# def fun(sum,n,i):
#     if i==n+1:
#         print(sum)
#         return
#     fun(sum+i,n,i+1)
# fun(0,10,0)

# function recursion: where the recusrsive funtion returns the answer and then it will prints . Here the printing is not done within the function
# my mehtod:
# def rec(n):
#     if n==0:
#         return 0
#     else:
#         return n+rec(n-1)
    
# sum=rec(10)
# print(sum)

# time complextiy is O(n) and space complexity is also O(n) beccause of n time calling any every tme each call is strored in stack space so it also reqer n slots each for one call return.you call space complexity as stack space in this program