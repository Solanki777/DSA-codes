class Solution:
    def pres(self,ch):
        if ch=='*' or ch=='/':
            return 2
        elif ch=='^':
            return 3
        elif ch=='+' or ch=='-':
            return 1
        else:
            return 0
        
    def infixtoPostfix(self, s):
        stack=[]
        ans=[]
        for ch in s:
            if ch.isalnum():
                ans.append(ch)
            
            elif ch=='(':
                stack.append(ch)
            
            elif ch==')':
                while stack and stack[-1]!='(':
                    ans.append(stack.pop())
                stack.pop()
            
            else:
                while (stack and 
                (self.pres(stack[-1]) > self.pres(ch) or
                (self.pres(stack[-1]) == self.pres(ch) and ch != '^'))):
                    ans.append(stack.pop())
                stack.append(ch)
                
                
                
               
        while stack:
            ans.append(stack.pop())
        
        return "".join(ans)



        