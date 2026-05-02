class Solution:
    def heapdown(self,arr,ind):
        smallest_ind=ind
        left_child=2*ind + 1
        right_child=2* ind +2
        
        if left_child<len(arr) and arr[left_child]<arr[smallest_ind]:
            smallest_ind=left_child
        if right_child<len(arr) and arr[right_child]<arr[smallest_ind]:
            smallest_ind=right_child
        
        if smallest_ind!=ind:
            arr[smallest_ind],arr[ind]=arr[ind],arr[smallest_ind]
            self.heapdown(arr,smallest_ind)
    
    def heapup(self,arr,ind):

        
        if ind>0 :
            parent=(ind-1)//2
            if arr[parent]>arr[ind]:
                arr[parent],arr[ind]=arr[ind],arr[parent]
                self.heapup(arr,parent)

    def minheap(self,arr,val,ind):
        arr[ind]=val
        parent=(ind-1)//2
        left_child=2*ind + 1
        right_child=2* ind +2

        if (left_child<len(arr) and arr[left_child]<arr[ind]) or (right_child<len(arr) and (arr[right_child]<arr[ind])):
            self.heapdown(arr,ind)
        elif ind>0 and arr[parent]>arr[ind]:
            self.heapup(arr,ind)

# TIme and space complexity is O(logn)

# implementing mean heap operations 
class Solu:
    def __init__(self,arr,count):
        self.arr=[]
        self.count=0
    
    def insertion(self,arr,count,val):
        sl=Solution()
        sl.minheap(arr,val,count)
        count+=1
