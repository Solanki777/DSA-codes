# finding largest the elements from the arry

# if arry is combination of positive and negative number then in begginnig you can tag large=float("inf") ar the first element of an arry


def fmax(arr):
    larger=arr[0]
    for el in range(1,len(arr)):
        larger=max(arr[el],larger)
    return larger
arr=[87,9,8,5,4,2,15,7,4,5,6,99]
ans=fmax(arr)
print(f"the larger number from the arry is {ans}")

# so here the time complexity is O(N) for whole loop traversling one by one to find the larger number and space complexity is O(1) Here we do not use any large space to store have complexity than 1 .