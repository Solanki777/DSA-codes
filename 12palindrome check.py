# this is mehtod used by me
# def check(str,last,first):
#     while(last>=first):
#         if(str[first]==str[last]):
#             first+=1
#             last-=1
#         else:
#             print("no")
#             break
        
#     if(last<=first):
#         print("yes")
#     else:
#         print("no")


# str=input("enter check the string is palindrome or not :")
# check(str,len(str)-1,0)

# using recursion
# def check(str,last,first):
#     if (last==first or last<first):
#         return True
#     elif(last>=first and str[last]==str[first]):
#         return check(str,last-1,first+1)
#     elif(str[last]!=str[first]):
#         return False

# str=input("enter check the string is palindrome or not :")
# ans=check(str,len(str)-1,0)
# if(ans):
#     print("string is palindrome")
# else:
#     print("string is not palindromen")