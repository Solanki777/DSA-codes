#User function Template for python3


class Solution:
    def preToInfix(self, pre_exp):
        stack=[]

        # traverse in reverse 
        for ch in reversed(pre_exp):

            # if it is operand push it into the stack 
            if ch.isalnum():
                stack.append(ch)
            else:
            # else pop two elements and put operand in middle of them 
                op1=stack.pop()
                op2=stack.pop()
                ans="("+op1+ch+op2+")"
                stack.append(ans)
        return stack[-1]
    