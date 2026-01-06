# 1.Binary Number Conversion:

#    9->1001 13->1101 so this is conversion of decimal to binary
    #  1001->9 1101-> vice versa also

# here the time complexity is O(logn) and also space complexity is O(logn) because each time their is devision and stroing each answer in result as output
# def conver2binary(num:int)->str:

#     if num==0:
#         return "0"
#     result=""

#     while num>0:

#         if num%2==1:
#             result+="1"

#         else:
#             result+="0"
#         num=num//2
    
#     result=result[::-1]
#     return result

# print(conver2binary(54861548))


# time complexity is O(len of string) and space complexity is O(1)
# def binary2digit(num:str)->int:
#     ans=0
#     power=0
#     index=len(num)-1

#     while index>=0:
#         ans+=(2**power)*int(num[index])
#         power+=1
#         index-=1

#     return ans

# print(binary2digit("10"))

# Some conceptual operations:

# 1. Swap two numbers in O(1) time and space complexity

# a=5
# b=10

# print("a is ",a^(a^b) )
# print("b is ",(a^b)^b )


# 2.check if ith bit is set or not

# using left shift 
# n=13
# i=1

# if n& (1<<i):
#     print("ith bit is set")
# else:
#     print("ith bit is not set")

# using right shift

# n=13
# i=2

# if ((n>>i)&1)==1:
#     print("bit is set")
# else:
#     print("bit is not set")


# 3.set the ith bit
# n=9
# i=2
# n=n|(1<<i)
# print("after setting ith bit:",n)

# 4.clear the ith bit
# n=13
# i=2 

# n=n&(~(1<<i))
# print("after clearing n th bit: ",n)

# 5.toggle the ith bit
# n=13
# i=2

# n=n^(1<<i)
# print("after toggling i th bit of n ",n)

# 6remove the last set bit from right side
# n=16
# print("after removing the ith bit answer is ",n&n-1)

# 7.check if the number is power of 2
n=16
if n&(n-1)==0:
    print("yes it is power of 2")
else:
    print("no it is not power of 2")

