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

 