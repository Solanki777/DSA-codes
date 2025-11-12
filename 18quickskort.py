def quicksort(arr,law,high):
    i,j=law,high
    pivot=arr[law]
    while(i<j):
        while(i<=high and pivot>=arr[i] ):
            # order is important in condition if you flip them here then they says order out of bound because if pivot is greter than arr[i] then it check for i<= high which already goes out of bound 
            i+=1
        while(j>=law and pivot<arr[j]):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[j],arr[law]=arr[law],arr[j]
    return j

def partition(arr,law,high):
    if(law<high):
        mid=quicksort(arr,law,high)
        partition(arr,law,mid-1)
        partition(arr,mid+1,high)

    return arr


arr=[9,8,7,6,5,4,3,2,1,0]
ans=partition(arr,0,len(arr)-1)
print(ans)