# def binary(arr,key):
#     low=0
#     high=len(arr)-1
#     while(low<=high):
#         mid=(low+high)//2
#         if key==arr[mid]:
#             return mid
#         elif key<arr[mid]:
#             high=mid-1
#         else:
#             low=mid+1
#     return -1

# arr=[0,1,2,3,4,5,6,7,8,9,10]
# key=1
# ans=binary(arr,key)
# if ans==-1:
#     print("answer not found")
# else: 
#     print("key is at index:",ans)


# using recursion:


def binary(arr,key,low,high):
    mid=(low+high)//2
    if(low<=high):
        if key==arr[mid]:
            return mid
        elif arr[mid]<key:
            return binary(arr,key,mid+1,high)
        else:
            return binary(arr,key,low,mid-1)
    else:
        return -1

arr=[0,1,2,3,4,5,6,7,8,9,10]
key=1
ans=binary(arr,key,0,len(arr)-1)
if ans==-1:
    print("answer not found")
else: 
    print("key is at index:",ans)

# timcomplexity for binary search is O(1) in best case else it is O(logn) and space compelxlity is O(1)