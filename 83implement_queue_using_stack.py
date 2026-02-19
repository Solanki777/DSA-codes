
class MyQueue:

    def __init__(self):
        self.stack=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    # when you pop the element all other will shift to left side so it give time complexity of O(n-1) and space complexity will be O(n)
    def pop(self) -> int:
        if len(self.stack)==0:
            return -1
        return self.stack.pop(0)
        

    def peek(self) -> int:
        if len(self.stack)==0:
            return -1
        x=self.stack[0]
        return x
        

    def empty(self) -> bool:
        if len(self.stack)==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()