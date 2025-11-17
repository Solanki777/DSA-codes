# here we rotating the arry in the right side by only one place
# example=[1,2,3,4,5,6,7,8,9]
# here we usa the consept of slicing where we slice the last element and than it merge with the the remiaining elemnets
# result=[9,1,2,3,4,5,6,7,8]

# usign slicing
# def right_rotate(arr):
#     # arr=arr[len(arr)-1 : ] + arr[0:len(arr)]
#     # here if you write same variable which already an arry than pyhon will automaticaly creates a new arry at diffrent location so for puting this elemnts in already arry then write like this:
    
#     arr[:]=arr[len(arr)-1 : ] + arr[0:len(arr)]
#     print(arr)
# arr=[1,2,3,4,5,6,7,8,9]
# right_rotate(arr)

# total time compelxity is O(n) for slicing copies having n elemnt and than again O(n) for concatenation of those number so total will be O(2n) which is equals to O(n) and space complxity would be O(n) for slicing n elemnts and store them their

# without slicing

def right_rotate(arr):
    last_element=arr[len(arr)-1]
    for el in range(-2,-len(arr)-1,-1):
        arr[el+1]=arr[el]
    arr[el]=last_element

    print(arr)



arr=[1,2,3,4,5,6,7,8,9]
right_rotate(arr)
