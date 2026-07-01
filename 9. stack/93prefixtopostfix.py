#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        stack=[]
        for ch in reversed(pre_exp):
            if ch.isalnum():
                stack.append(ch)
            else:
                op1=stack.pop()
                op2=stack.pop()
                ans=op1+op2+ch
                stack.append(ans)
        return stack[-1]