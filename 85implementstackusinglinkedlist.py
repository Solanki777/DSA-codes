# Node class
''' class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None 
'''

# Stack class template
class myStack:

    def __init__(self):
        self.top=None
        self.count=0
        # Initialize your data members
        

    def isEmpty(self):
        return self.top is None
        # Check if the stack is empty
        

    def push(self, x):
        new_node=Node(x)
        new_node.next=self.top
        self.top=new_node
        self.count+=1
       
        # Adds element x to the top of the stack
        

    def pop(self):
        if self.isEmpty():
            return -1
        
        temp=self.top
        self.top=self.top.next
        self.count-=1
        return temp.data
    

        # Removes an element from the top of the stack


    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.isEmpty():
            return -1
        return self.top.data


    def size(self):
        return self.count
        # Returns the current size of the stack