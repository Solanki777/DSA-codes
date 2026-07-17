class Solution:
    def recursion(self,arr,n):
        if n ==1 :
            return
        
        for i in range(n-1):
            if arr[i] > arr[i+1] :
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
        self.recursion(arr,n-1)
    def bubbleSort(self,arr):
        self.recursion(arr,len(arr))

# TIme complexity is O(n^2) and space complexity is O(1)