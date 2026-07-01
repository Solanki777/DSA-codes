# my solution:
# def remove_duplicate(arr):
#     count=0
#     new_arr=[]
#     for el in range(0,len(arr)-1):
#         if arr[el]==arr[el+1]:
#             count+=1
#         else:
#             new_arr.append(arr[el])
#     new_arr.append(arr[el])
#     print("arr is ",new_arr)
#     return count

# arr=[1,1,2,2,3,4,4,4,5,5,6,6,7,8,8,9,9]
# ans=remove_duplicate(arr)
# print("total number of duplicates are: ",ans)
# time and space complexity is O(n)

# usign dictionary
# # code by debug method


# def remove(arr):
    
#     freq_map={}
#     for i in range(len(arr)):
#         freq_map[arr[i]]=0
    
#     j=0
#     for k in freq_map:
#         arr[j]=k
#         j+=1
#     print("arry is ",arr)
#     return j
# arr=[1,1,1,2,2,2,2,3,4,4,4,4,5,6,6,6,7,8,8,8,9,9,9]
# count=remove(arr)
# print("total duplicates are : ",count)

# Time complexity is O(2N) and space compelixity is O(N)

# Otimal solllution


def remove(arr):
    i=0
    j=1
    while(j<=len(arr)-1):
        if arr[i]==arr[j]:
            j+=1
        else:
            i+=1
            arr[i]=arr[j]


    print("sorted arr:",arr)
    print("number os disctinct values:",i+1) # because i starts form 0
arr=[1,1,1,2,2,2,2,3,4,4,4,4,5,6,6,6,7,8,8,8,9,9,9]
remove(arr)

# here the time complexity is O(n) and space compelxity is O(1)