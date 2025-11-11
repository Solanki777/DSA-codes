# def merge_sort(left,right):
#     m=len(left)
#     n=len(right)
#     i,j=0,0
#     result=[]
#     while(i<m and j<n):
#         if left[i]<right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     while(i<m):
#         result.append(left[i])
#         i+=1
#     while(j<n):
#         result.append(right[j])
#         j+=1
#     return result

# def divide(arr):
#     if len(arr)<=1:
#         return arr
#     else:
#         mid=len(arr)//2
#         left_arr=arr[:mid]
#         right_arr=arr[mid:]
#         left=divide(left_arr)
#         right=divide(right_arr)
#         return merge_sort(left,right)

# a=[9,8,7,6,5,4,3,2,1]
# ans=divide(a)

# print(ans)

# if any thing is dividing hald in each iteration then time complextiy is log N so here the complexity for divide function is logN and for merge the loops runs ans all value stored in result which is size of n so total time complexity become O(NlogN) and space compelity is O(N) for storing ans into result

def reverse_merge(left,right):
    i,j=0,0
    m,n=len(left),len(right)
    result=[]

    while(i<m and j<n):
        if left[i]>right[j]:
            result.append(left[i])
            i+=1

        else:
            result.append(right[j])
            j=+1

    while(i<m):
        result.append(left[i])
        i+=1

    while(j<n):
        result.append(right[j])
        j+=1

    return result

def divide(arr):
    if len(arr)==1:
        return arr
    else:
        mid=len(arr)//2
        left=divide(arr[:mid])
        right=divide(arr[mid:])
        ans=reverse_merge(left,right)
        return ans
    
a=[9,8,7,6,5,4,3,2,1]
ans=divide(a)

print(ans)

