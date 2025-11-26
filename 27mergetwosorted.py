# merge two sorted array

# my method
# def duplicate(arr3):
#     i=0
#     j=1
#     while j<len(arr3):
#         if(arr3[j]==arr3[i]):
#             j+=1
#         else:
#             i+=1
#             arr3[i]=arr3[j]
#     print(arr3)

# def mergesorted(arr1,arr2):
#     l1=len(arr1)
#     l2=len(arr2)
#     i=0
#     j=0
#     arr3=[]
#     while(i<l1 and j<l2):
#         if(arr1[i]>arr2[j]):
#             arr3.append(arr2[j])
#             j+=1
#         else:
#             arr3.append(arr1[i])
#             i+=1
#     while(i!=l1):
#         arr3.append(arr1[i])
#         i+=1
#     while(j!=l2):
#         arr3.append(arr2[j])
#         j+=1
#     print(arr3)
#     duplicate(arr3)
        


# arr1=[1,1,2,2,3,4,5,5,6,6]
# arr2=[1,2,3,3,4,5,6,7,8,9,9,10]
# mergesorted(arr1,arr2)

# effective method



def mergesorted(arr1,arr2):
    l1=len(arr1)
    l2=len(arr2)
    i=0
    j=0
    arr3=[]
    while i<l1 and j<l2:
        if (arr1[i]<=arr2[j]):
            if len(arr3)==0 or arr3[-1]!=arr1[i]:
                arr3.append(arr1[i])
            i+=1
        else:
            if len(arr3)==0 or arr3[-1]!=arr2[j]:
                arr3.append(arr2[j])
            j+=1
        
    while i<l1:
        if len(arr3)==0 or arr3[-1]!=arr1[i]:
            arr3.append(arr1[i])
        i+=1
    while j<l2:
        if len(arr3)==0 or arr3[-1]!=arr2[j]:
            arr3.append(arr2[j])
        j+=1
    print(arr3)

arr1=[1,1,2,2,3,4,5,5,6,6]
arr2=[1,2,3,3,4,5,6,7,8,9,9,10]
mergesorted(arr1,arr2)


# time complexity is O(M+N) for travelig both loop and space complexity is O(N) where we take a new arry for merging sorted arry with uniq values
