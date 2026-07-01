# def insertion(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while j>=0 and arr[j]>=key:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
#     print(arr)

# arr=[9,8,7,6,5,4,3,2,1,0]
# insertion(arr)
#     # time complexity is O(n^2) two loop runs overall two times and space complexity is O(1)

def rev_insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]<=key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    print(arr)

arr=[1,2,3,4,5,6,7,8,9,0]
rev_insertion(arr)
