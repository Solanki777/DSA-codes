from collections import deque
class MyStack:

    def __init__(self):
        self.queue=deque()
        
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        

    def pop(self) -> int:
        if len(self.queue)==0:
            return "stack is empty"
        return self.queue.popleft()
        

    def top(self) -> int:
        if len(self.queue)==0:
            return " empty stack "
        return self.queue[0]
        

    def empty(self) -> bool:
        if len(self.queue)==0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# only pyshing an element takes O(n-1) time complexity other takes O(1)  and space complexity is O(n)