# Normal Method:
# def bubble(arr):
#     n=len(arr)
#     for i in range(0,n-1):
#         for j in range(0,n-1-i):
#             if arr[j]>=arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     print(arr)

# arr=[5,7,8,9,6,2,1,4,3]
# bubble(arr)

# in this ordinary method time compelxity is O(n^2) in all case but we can retuse it if we set flag at swapping . IF arr[j]>=arr[j+1] than and only than we have to profrm swap else we dont need to perform the swaaping Process

def bubble(arr):
    n=len(arr)
    for i in range(0,n-1):
        swapp=False
        for j in range(0,n-1-i):
            if arr[j]>=arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapp=True
        if not swapp:
            # if there is no swapp in first iteration then our arry is already sorted there is no need of going further for sorting in best case
            break
            
    print(arr)

arr=[5,7,8,9,6,2,1,4,3]
bubble(arr)

# in above case if arry is already sorted in best case where first loop comparision is done through an arry which check one by one so if set a flag if arry is already sorted than there is not need go further after the first iteration.So in best case the time complexity is O(n).And for space complexity in over all case is (1). we do not store any arry . we only stores a single variable so it is equls to 1 overall the code.