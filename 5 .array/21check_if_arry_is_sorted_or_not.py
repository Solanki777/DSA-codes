def check(arr):
    for el in range(0,len(arr)-1):
        if arr[el]>arr[el+1]:
            return False
    return True


arr=[1,2,3,4,5,6,7,8,9]
b=check(arr)
print("arry is sorted?:",b)

# Time complexity is O(N) and space complexity is O(1)