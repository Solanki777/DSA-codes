
# # brute force solution: time complexity is O(n^2) and space complexity is O(1)
# def find_single(arr):
#     for i in range(len(arr)):
#         found=False
#         for j in range(i+1,len(arr)):
#             if i!=j and arr[i]==arr[j]:
#                 found=True
#                 break
#             if not found:
#                 return arr[i]

# arr=[5,1,3,3,7,1,7]
# # here 5 not returns twise so return it
# print(find_single(arr))

# optimal soution

def find_single(arr):
    el=0
    for i in range(len(arr)):
        el ^=arr[i]
    return el


arr=[5,1,3,3,7,1,7]
print(find_single(arr))