class Solution:
    def postToInfix(self, postfix):
        # here we give a postfix
        # here the operations are reverse we push the operad into the stack 
        # if any operator is ancounter we pop 2 operands from the stack
        # and put the operator between them push into the stack 

        stack=[]
        
        for ch in postfix:
            if ch.isalnum():
                stack.append(ch)
            else:
                op2=stack.pop()
                op1=stack.pop()
                ans="("+op1+ch+op2+")"
                stack.append(ans)
        return stack[-1]