class Solution:
    def recursion(self , n , arr ):
        if n == 1:
            return
        
        self.recursion(n-1,arr)
        
        key = arr[n-1]
        j = n-2
        
        while j>=0 and arr[j] > key :
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    
    def insertionSort(self, arr):
        n = len(arr)
        self.recursion(n,arr)
        return arr

# time complexity is O(n^2) and space compelxity is O(1)