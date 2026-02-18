class myQueue:
    def __init__(self, n):
        self.arry=[]
        self.size=n

    
    def isEmpty(self):
        if len(self.arry)==0:
            return True
        return False
        
        # Check if queue is empty

    
    def isFull(self):
        if len(self.arry)==self.size:
            return True
        return False
        # Check if queue is full

    
    def enqueue(self, x):
        if len(self.arry)==self.size:
            return -1
        self.arry.append(x)
        return
        # Enqueue

    
    def dequeue(self):
        if len(self.arry)==0:
            return -1
        self.arry.pop(0)
        return
        # Dequeue

    
    def getFront(self):
        if len(self.arry)==0:
            return -1
        return self.arry[0]
        # Get front element
       
    
    def getRear(self):
        if len(self.arry)==0:
            return -1
        return self.arry[len(self.arry)-1]
        # Get rear element 
        
# only dqueue has time complexity of O(n) and all other operation has time and space omplexity of O(!)