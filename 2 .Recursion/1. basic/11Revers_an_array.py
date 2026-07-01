
# ordinary method without recursion
# def rev(nums):
#     rev_arry=[]
#     for el in range(len(nums)-1,-1,-1):
#             rev_arry.append(nums[el])
    
#     print(rev_arry)


# nums=[1,2,3,4,5,6,7,8,9]
# rev(nums)

# my method
# def rev(arr,last,first,rev_arry=[]):
#     if first>last:
#         return rev_arry
#     else:
#         rev_arry.append(arr[last])
#         return rev(arr,last-1,first)

# arr=[1,2,3,4,5,6,7,8,9]
# ans=rev(arr,len(arr)-1,0)
# print(ans)

# method by using swapping 
def rec(arr,left,right):
    if left==right:
        return arr
    else:
        arr[left],arr[right]=arr[right],arr[left]
        return rec(arr,left+1,right-1)
    



arr=[1,2,3,4,5,6,7,8,9]
print(rec(arr,0,len(arr)-1))

# time complity and space complexity is O(n/2) because their widd half operation of size of arry and that will stored in stack space . So it becomes O(n/2)