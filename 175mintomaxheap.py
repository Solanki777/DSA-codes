class Solution:
    def mintomaxheap(self,arr):
        n=len(arr)
        st=n//2-1

        def heapify(index):
            left=index*2+1
            right=index*2+2
            big=index

            if left<n and arr[left]>arr[big]:
                big=left
            if right<n and arr[right]>arr[big]:
                big=right
            if big!=index:
                arr[big],arr[index]=arr[index],arr[big]
                heapify(big)

        for i in range(st,-1,-1):
            heapify(i)

class Solution:
    def maxtominheap(self,arr):
        n=len(arr)
        st=n//2-1

        def heapify(index):
            left=index*2+1
            right=index*2+2
            small=index

            if left<n and arr[left]<arr[small]:
                small=left
            if right<n and arr[right]<arr[small]:
                small=right
            if small!=index:
                arr[small],arr[index]=arr[index],arr[small]
                heapify(small)

        for i in range(st,-1,-1):
            heapify(i)

# Time complexity is O(n) and space complexity is O(1)