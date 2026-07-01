# def quicksort(arr,law,high):
#     i,j=law,high
#     pivot=arr[law]
#     while(i<j):
#         while(i<=high and pivot>=arr[i] ):
#             # order is important in condition if you flip them here then they says order out of bound because if pivot is greter than arr[i] then it check for i<= high which already goes out of bound 
#             i+=1
#         while(j>=law and pivot<arr[j]):
#             j-=1
#         if(i<j):
#             arr[i],arr[j]=arr[j],arr[i]
#     arr[j],arr[law]=arr[law],arr[j]
#     return j

# def partition(arr,law,high):
#     if(law<high):
#         mid=quicksort(arr,law,high)
#         partition(arr,law,mid-1)
#         partition(arr,mid+1,high)

#     return arr


# arr=[9,8,7,6,5,4,3,2,1,0]
# ans=partition(arr,0,len(arr)-1)
# print(ans)

# quick sort in reverse:
def partition(arr,law,high):
    pivot=arr[law]
    i,j=law,high
    while(i<j):
        while i<=high and arr[i]>=pivot:
            i+=1
        while j>=law and arr[j]<pivot :
            j-=1
        if i<j :
            arr [i],arr[j]=arr[j],arr[i]
    arr[law],arr[j]=arr[j],arr[law]
    return j



def quick_sort(arr,law,high):
    if (law<high):
        mid=partition(arr,law,high)
        quick_sort(arr,mid+1,high)
        quick_sort(arr,law,mid-1)
    return arr

arr=[1,2,3,4,5,6,7,8,9]
ans=quick_sort(arr,0,len(arr)-1)
print(ans)


# here also divide and solve is used in quick_sort so fot that the time complexity is in best and average case :O(logn) and for partion it runs n times for each element so overall timecomplexity is O(nlogn) and ther is no storing arr in any extra space so space complexity is O(1)

# but in worst case like all numbers are 5 in arry so every time i and j so from end of the arry means  N and for N elements so it becomes O(n^2)