#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        stack=[]
        for ch in post_exp:
            if ch.isalnum():
                stack.append(ch)
            else:
                op2=stack.pop()
                op1=stack.pop()
                ans=ch+op1+op2
                stack.append(ans)
        return stack[-1]
