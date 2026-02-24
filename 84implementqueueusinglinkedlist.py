# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        self.front=None
        self.rare=None
        self.cont=0
        

    def isEmpty(self):
        return self.front is None
        # Return True if queue is empty, else False
        

    def enqueue(self, x):
        new_node=Node(x)

        if self.rare is None:
            self.front=self.rare=new_node
        else:
            self.rare.next=new_node
            self.rare=new_node
        self.cont+=1
        # Add element x to the rear
        

    def dequeue(self):
        if self.isEmpty():
            return -1
        
        temp=self.front
        self.front=self.front.next

        if self.front is None:
            self.rare=None
        self.cont-=1
        return temp.data
        # Remove the front element


    def getFront(self):
        if self.isEmpty():
            return -1
        return self.front.data
        # Return front element
        # return -1 if empty


    def size(self):
        return self.cont
        # Return current size
