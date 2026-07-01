class Solution:
    def isminheap(self,arr):
        n=len(arr)
        def is_valid(index):
            leftchild=index*2+1
            rightchild=index*2+2
            if leftchild<len(arr) and arr[leftchild]<arr[index]:
                return False
            if rightchild<len(arr) and arr[rightchild]<arr[index]:
                return False
            return True
        
        for i in range(len(arr)//2):
            if not is_valid(i):
                return False
        return True


class Solution:
    def ismax_heap(self,arr):
        n=len(arr)
        def is_valid(index):
            left=2*index+1
            right=2*index+2

            if left<n and arr[left]>arr[index]:
                return False
            if right<n and arr[right]>arr[index]:
                return False
            return True


        for i in range(len(arr)//2):
            if not is_valid(i):
                return False
        return True

        


# TIme complexity is O(n/2) and space complexity is(1)