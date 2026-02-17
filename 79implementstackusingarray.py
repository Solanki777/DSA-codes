class myStack:
    def __init__(self, n):
        # build the list which we use in stack 
        self.size=n
        self.items=[]
    
    def isEmpty(self):
        return len(self.items)==0

    
    def isFull(self):
        # Check if stack is full
        return len(self.items)==self.size


    
    def push(self, x):
        # Insert x at the top of the stack
        if len(self.items)==self.size:
            return -1
        self.items.append(x)

    
    def pop(self):
        # Removes an element from the top of the stack
        if len(self.items)==0:
            return -1
        x=self.items.pop()
        return x

    
    def peek(self):
        # Returns the top element of the stack
        if len(self.items)==0:
            return -1
        return self.items[-1]
    
stack=myStack(5)
print(stack.isEmpty())
print(stack.isFull())
print(stack.push(43))
print(stack.push(234))
print(stack.peek())
print(stack.isEmpty())
print(stack.isFull())
print(stack.peek())
print(stack.pop())

# time complexity is O(1) for all and space complexity is O(n)