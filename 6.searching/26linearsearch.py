def linear(arr,key):
    for el in range(len(arr)):
        if arr[el]==key:
            return el
    return "not found"
        

arr=[1,2,3,4,5,6,7,8,9]
key=8
pos=linear(arr,key)
print(pos)

# time complexity is O(n) and space complexity is 1
