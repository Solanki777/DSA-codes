# implementing max heap operations 
class Solution:
    def __init__(self):
        self.arr=[]
        self.count=0

    def heapifydown(self,arr,ind):
        left=ind*2+1
        right=ind*2+2
        small=ind

        if left<len(arr) and arr[left]>arr[small]:
            small=left
        
        if right<len(arr) and arr[right]>arr[small]:
            small=right

        if small!=ind:
            arr[small],arr[ind]=arr[ind],arr[small]
            self.heapifydown(arr,small)
    
    def heapifyup(self,arr,ind):
        if ind>0:
            parent=(ind-1)//2
            if arr[parent]<arr[ind]:
                arr[parent],arr[ind]=arr[ind],arr[parent]
                self.heapifyup(arr,parent)
        


    def initlize(self):
        self.arr=[]
        self.count=0
    
    def insert(self,val):
        self.arr.append(val)
        self.count+=1
        self.heapifyup(self.arr,self.count-1)
    
    def getmax(self):
        if self.count>0:
            return self.arr[0]
        return None
    
    def extractmax(self):
        if self.count>0:
            
            self.arr[0],self.arr[self.count-1]=self.arr[self.count-1],self.arr[0]
            temp=self.arr.pop()
            self.count-=1
            self.heapifydown(self.arr,0)
            return temp
        return None
    
    def isempty(self):
        return self.count==0
    
    def size(self):
        return self.count
    
    def changekey(self, val, ind):
        old = self.arr[ind]

        if val > old:
            self.arr[ind] = val
            self.heapifyup(self.arr, ind)
        else:
            self.arr[ind] = val
            self.heapifydown(self.arr, ind)



        