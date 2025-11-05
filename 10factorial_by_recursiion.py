def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)



ans=fact(5)
print("factorial fo the number is ", ans)

# time complextiy is O(n) and space complexity is also O(n) beccause of n time calling any every tme each call is strored in stack space so it also reqer n slots each for one call return.you call space complexity as stack space in this program