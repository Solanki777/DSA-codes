# my method:

# def rotate(nums,rotation):
#     i=1
#     l=len(nums)-1
#     while(rotation>=i):
#         p=l
#         while(p!=0):
#             nums[p-1],nums[p]=nums[p],nums[p-1]
#             p-=1
#         i+=1

#     print(nums)

# nums=[1,2,3,4,5,6,7,8,9]
# rotation=int(input("enter a number you want to rotate"))

# rotate(nums,rotation)


# time complexity is O(rotation*n) and space complexity is 



# Other solution:
# here supose their are k rotation . if we have to rotate=len(arr)-1 than the same arry we have to return . so in each time we do rotation than time complexity will be goes where far. Here first we find modulo with length of arry than we pop the last element and pust it to 0th index in starting 
# def rotate(nums,rotation):
#     k=rotation%len(nums)
#     print(k)

#     for el in range(0,k):
#         e=nums.pop()
#         nums.insert(0,e)
#     print(nums)


# nums=[1,2,3,4,5,6,7,8,9]
# rotation=int(input("enter a number you want to rotate"))
# rotate(nums,rotation)

# in this we uses the pop and insert function of the python to do the k rotation as you can we simply pop the last element and pust it to the first place.For the time complexity for pop the element it requires len(nums-1) time and than working with 0 to k the total time complexity is O(e*k) and space complexity is O(1)


# using slicing
# here we like slicing the k elements from the arry where k is the number of rotation required in the arry. Here we do a slice of that particular arry and insert it at the begginig of the arry

# def rotate(nums,k):
#     l=len(nums)-1
#     nums[:]=nums[l-k+1:]+nums[0:l-k+1]
#     print(nums)


# nums=[1,2,3,4,5,6,7,8,9]
# k=int(input("enete a number of rotate you want:"))
# rotate(nums,k)

# time complexity becomes L-K+1+L-K+1=2L means O(L) and space complexity is O(1)


# other optimal solution without using slicing
# get 2 strings than a part where to we have to rotating than we rotate both part and revrse the arry
# like k=5
# len(arr)-k+1 means= arr1 is 5 to len(arr)
# in starting means=arr2 is 0 to 4 
# reverse both arry arr1 
# then reverse whole arry and we got the answer


nums=[1,2,3,4,5,6,7,8,9]

def reverse(left,right):
    while(right>left):
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return
    


k=int(input("enete a number of rotate you want:"))
l=len(nums)
reverse(0,l-k-1)
reverse(l-k,l-1)
reverse(0,l-1)
print(nums)

# here the same time complexity as the above and space complity also