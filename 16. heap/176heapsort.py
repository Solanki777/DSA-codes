
class Solution:
    def heapify(self,index,arr,n):
            left=index*2+1
            right=index*2+2
            big=index

            if left<n and arr[left]>arr[big]:
                big=left
            if right<n and arr[right]>arr[big]:
                big=right
            if big!=index:
                arr[big],arr[index]=arr[index],arr[big]
                self.heapify(big,arr,n)

    def heap_sort(self,arr):
        n=len(arr)

        for i in range(n//2-1,-1,-1):
            self.heapify(i,arr,n)
        
        for i in range(n-1,0,-1):
            arr[0],arr[i]=arr[i],arr[0]
            self.heapify(0,arr,i)
        return arr

# Time complexity is O(nlogn) and space complexity is O(logn)