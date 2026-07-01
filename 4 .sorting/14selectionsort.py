
# selection sort for assending order:
# def selection_sort(arr,n):
#     for i in range(0,n):
#         min=i
#         for j in range(i+1,n):
#             if arr[min]>arr[j]:
#                 min=j
#         if i!=min:
#             arr[i],arr[min]=arr[min],arr[i]
#     print(arr)

# arr=[8,4,5,6,9,7,2,1,5,4,8,6,3,2]
# selection_sort(arr,len(arr))
# time complexity is O(n^2) because two loops going to n and space complexity is O(1)


# selection sort fokr descending order:
def selection_sort(arr,n):
    for i in range(0,n):
        max=i
        for j in range(i+1,n):
            if arr[max]<arr[j]:
                max=j
        if j!=max:
            arr[max],arr[i]=arr[i],arr[max]

    print(arr)

arr=[8,4,5,6,9,7,2,1,5,4,8,6,3,2]
selection_sort(arr,len(arr))