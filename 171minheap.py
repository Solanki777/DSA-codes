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

class Solution:
    def __init__(self):
        self.arr=[]
        self.count=0
    
    def heapifyup(self,arr,ind):
        parent=(ind-1)//2
        if ind>0 and arr[ind]<arr[parent]:
            arr[ind],arr[parent]=arr[parent],arr[ind]
            self.heapifyup(arr,parent)
        
    def heapifydown(self,arr,ind):
        smalle=ind
        n=len(arr)
        left=2*ind+1
        right=2*ind+2

        if left<n and arr[left]< arr[smalle]:
            smalle=left
        if right<n and arr[right] < arr[smalle]:
            smalle=right
        
        if smalle!=ind:
            arr[smalle],arr[ind]=arr[ind],arr[smalle]
            self.heapifydown(arr,smalle)
    
    def initialization(self):
        self.arr.clear()
        self.count=0
    
    def insert(self,key):
        self.arr.append(key)
        self.heapifyup(self.arr,self.count)
        self.count+=1
    
    def changekey(self,index,new_val):
        if self.arr[index] > new_val:
            self.arr[index]=new_val
            self.heapifyup(self.arr,index)
        else:
            self.arr[index]=new_val
            self.heapifydown(self.arr,index)
    
    def extracmin(self):
        if self.count==0:
            return None
        ele=self.arr[0]
        self.arr[0],self.arr[self.count-1]=self.arr[self.count-1],self.arr[0]
        self.arr.pop()
        self.count-=1
        if self.count>0:
            self.heapifydown(self.arr,0)
        return ele
    
    def isempty(self):
        return self.count==0
    def getMin(self):
        return self.arr[0] if self.count>0 else None
    def heapsize(self):
        return self.count
    
