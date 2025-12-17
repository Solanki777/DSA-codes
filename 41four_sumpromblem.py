# buteforce solution
# def foursum(arr):
#     n=len(arr)
#     ans=set()
#     if n==0 :
#         return []
#     for i in range(0,n-3):
#         for k in range(i+1,n-2):
#             for l in range(k+1,n-1):
#                 for m in range(l+1,n):
#                     if arr[i]+arr[k]+arr[l]+arr[m]==0:
#                         temp=(arr[i],arr[k],arr[l],arr[m])
#                         temp=tuple(sorted(temp))

#                         ans.add(temp)

#     return ans


# arr=[1,0,-1,0,-2,2,5,9]
# result=foursum(arr)
# print(result)


# time complexity is O(n^4) and space complexity is O(k) k = number of valid unique quadruplets

# better solution: in better solution we gona run three loop and find the four elemnt
# def foursum(arr):
#     n=len(arr)
#     result=set()
#     if n<4:
#         return []
#     for i in range(0,n-3):
#         for j in range(i+1,n-2):
#             temp=set()
#             for k in range(j+1,n-1):
#                 fourth=-(arr[i]+arr[j]+arr[k])
#                 if fourth in temp:
#                     t=(arr[i],arr[j],arr[k],fourth)
#                     t=tuple(sorted(t))
#                     result.add(t)
#                 temp.add(arr[k])
#     return result

# timecomplexity is O(N^3) and space compelxity is O(N)

# arr=[1,0,-1,0,-2,2,5,9]
# result=foursum(arr)
# print(result)

# otimal solution
def foursum(arr,target):
    arr.sort()
    n=len(arr)
    if n<4:
        return []
    
    result=set()
    for i in range(0,n-3):
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and arr[j]==arr[j-1]:
                continue
            l=j+1
            k=len(arr)-1
            while l<k:
                s=arr[i]+arr[j]+arr[k]+arr[l]
                if s==target:

                    temp=(arr[i],arr[j],arr[l],arr[k])
                    temp=tuple(temp)
                    result.add(temp)
                    l+=1
                    k-=1
                    while l<k and arr[l]==arr[l-1]:

                        l+=1
                    while l<k and arr[k]==arr[k+1]:
                        k-=1
                elif s>target:
                    k-=1
                else:
                    l+=1
    return result

# time complexity is O(N^3) and space compelxity O(no. of ans)

arr=[1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6] 
target=8
result=foursum(arr,target)
print(result)
