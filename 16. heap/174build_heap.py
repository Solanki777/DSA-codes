# class Solution:
#     def heapify(self,index,arr):
#         n=len(arr)
#         left=index*2+1
#         right=index*2+2
#         big=index


#         if left<n and arr[left]>arr[big]:
#             big=left
#         if right<n and arr[right]>arr[big]:
#             big=right
        
#         if big!=index:
#             arr[big],arr[index]=arr[index],arr[big]
#             self.heapify(big,arr)            


# # brute force like checking for childs are waste of time 
#     # def build_heap_max(self,arr):
#     #     for i in range(-1,-1,-1):
#     #         self.set(i,arr)
    
#     def build_heap_max(self,arr):
#         for i in range(len(arr)//2-1,-1,-1):
#             self.heapify(i,arr)

# time complexity is O(n) and space complexity is O(1)
class Solution:
    def heapify(self,index,arr):
        n=len(arr)
        left=index*2+1
        right=index*2+2
        small=index


        if left<n and arr[left]<arr[small]:
            small=left
        if right<n and arr[right]<arr[small]:
            small=right
        
        if small!=index:
            arr[small],arr[index]=arr[index],arr[small]
            self.heapify(small,arr)            



    def build_heap_min(self,arr):
        for i in range(len(arr)//2-1,-1,-1):
            self.heapify(i,arr)


# time complexity is O(n) and space complexity is O(1)