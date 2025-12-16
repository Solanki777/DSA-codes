# def three_sum(arr):
#     ans=[]
#     for i in range(len(arr)-1):
#         for j in range(i+1,len(arr)-1):
#             for k in range(j+1,len(arr)-1):
                    
#                     if (arr[i]+arr[j]+arr[k])==0:
#                         ans.append(tuple(sorted([arr[i],arr[j],arr[k]])))

# # tuple:immutable,allow duplicates(),can stored in set and list.
# # list:mutable,allow duplicates [],not stored in set and but can be tuple
# # set:mutable,distict values{}, not stored in set or tuple

#     return ans


# # time complexity is O(N^3) and space complexity is O(no of tuples inside the set)



# arr=[-1,0,1,2,-1,-4]

# my_set=set(three_sum(arr))
# print(my_set)

# # here we have to pick 3 diffrenet variable from the list and sum of those number should be zero. you can not take 3 same variable at the same palce twice (No duplicate allowed) and also you can not take 1 place varibale twice.


# now go for better solution 

# we have equation (arr[i]+arr[j]+arr[k])==0: right if we place the arr[i]+arr[j] at the right side then we can find the arr[k] like:arr[k]=-(arr[i]+arr[j]) then we have to find arr[k] is exits or not in set or disction (becuase both take O(1)) to find the number.


# better solution now we gona use here 2 loops only
# def three_sum(arr):
#     ans=set()
#     for i in range(len(arr)):
#         my_set=set()
#         for j in range(i+1,len(arr)):
#             third=-(arr[i]+arr[j])
#             if third in my_set:
#                 temp=[arr[i],arr[j],third]
#                 temp.sort()
#                 ans.add(tuple(temp))

#             # this stores i and j 's between values to remove duplicates
#             my_set.add(arr[j])

#     return ans

# arr=[-1,0,1,2,-1,-4]

# my_set=three_sum(arr)
# print(my_set)

# here the time compelxity is O(n^2) and space complexity is O(N) overall 

# otimal solution

def three_sum(arr):
    # sortes the arr
    arr.sort()
    # [-1, -1, -1, -1, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]
    ans=[]
    n=len(arr)

    for i in range(n-2):
        if i>0 and arr[i]==arr[i-1]:
            continue

        left=i+1
        right=n-1

        while left<right:
            s=arr[i]+arr[left]+arr[right]
            if s==0:
                t=tuple([arr[i],arr[left],arr[right]])
                ans.append(t)

                left+=1
                right-=1

                while left<right and arr[left]==arr[left-1]:
                    left+=1
                while left<right and arr[right]==arr[right+1]:
                    right-=1
                
            elif s>0:
                right-=1
            else:
                left+=1
    return ans

                

arr=[-1,0,1,2,-1,-1,1,0,1,2,2,-1,0,1]

my_set=three_sum(arr)
print(my_set)

# time complexity is O(N^2) but space complexity reduces to O(1)