class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=float('inf')
        

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.mini=val
            self.stack.append([val,self.mini])
        else:
            self.mini=min(self.mini,val)
            self.stack.append([val,self.mini])
        

    def pop(self) -> None:
        if len(self.stack)==0:
            return -1
        else:
            temp=self.stack.pop()
            if len(self.stack)==0:
                self.mini=float('inf')
                return 
            else:
                self.mini=self.stack[-1][1]
            return temp[0]
    


    def top(self) -> int:
        if len(self.stack)==0:
            return -1
        temp=self.stack[-1]
        return temp[0]
        
    # time complexity is O(1)
    def getMin(self) -> int:
        if len(self.stack)==0:
            return -1
        temp=self.stack[-1]
        return temp[1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()