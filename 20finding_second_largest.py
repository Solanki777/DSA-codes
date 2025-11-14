# # my method:if there is 2 or having more elements having same value then  they are not considerd


# def second(arr):
#     larger=arr[0]
#     i=0
#     while(i<=len(arr)-1):
#         if larger<arr[i]:
#             larger=arr[i]
#         i+=1
#     print("larger value is ",larger)
#     new_arry=[]

#     i=0
#     while(i<=len(arr)-1):
#         if arr[i]==larger:
#             exit
#         else:
#             new_arry.append(arr[i])
#         i+=1
#     print(new_arry)

#     second_large=new_arry[0]
#     i=0
#     while(i<=len(new_arry)-1):
#         if second_large<new_arry[i]:
#             second_large=new_arry[i]
#         i+=1
#     print("Secound larger value is ",second_large)

# arr=[45,12,45,78,5,4,9,65,45,15,23,99,98]
# second(arr)


# precondition:all elements in arry should by desctict
# for values are distinct:

# simple solution first sort the arry than return the second last element from the arry
# def second(arry):
#     new_arry=sorted(arry)
#     print("the sorted arry",new_arry)
#     return new_arry[len(new_arry)-2]

# arry=[45,12,45,78,5,4,9,65,45,15,23,99,98]
# ans=second(arry)
# print("the second large number is ",ans)

# here the time complexity is O(nlogn) which is like used sorting methoda and space complexity is O(1)

# other simple solution:
# def second(arry):
#     i=0
#     largest=float("-inf")
#     s_largest=float("-inf")

#     while i<=len(arry)-1:
#         largest=max(largest,arry[i])
#         i+=1
    
#     i=0
#     while i<=len(arry)-1:
#         if(largest!=arry[i] and s_largest<arry[i]):
#             s_largest=arry[i]
#         i+=1
#     print(largest)
#     print(s_largest)

# arry=[45,12,45,78,5,4,9,65,45,15,23,99,98]
# second(arry)

# time complexitiy is O(n+n) means O(N) and space complexity is O(1)

# Optimal solution : we do this in single iteration so time complexity is become O(N) 

def secound_large(arr):

    large=float("-inf")
    s_large=float("-inf")

    for el in range(len(arr)):

        if arr[el]>large:
            if large!=s_large:
                s_large=large
            large=arr[el]
            
        elif arr[el]>s_large and large!=arr[el]:
            s_large=arr[el]
        
    print(large)
    print(s_large)


arr=[1,2,3,4,5,6,7,8,9,10]
secound_large(arr)

here the time complexity is O(n) and space complexity is 1

