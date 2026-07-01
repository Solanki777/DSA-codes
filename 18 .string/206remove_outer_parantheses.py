#  using stack 
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=[]
        index=[]
        stack=[]
        for index in range(len(s)):
            if s[index]=='(':
                stack.append(index)
                if len(stack)>1:
                    ans.append(s[index])
                    
            else:
                if len(stack)>1:
                    ans.append(s[index])
                stack.pop()
        return "".join(ans)


#space optimization : time complexity is O(n) and space complexity is O(1) 
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth=0
        ans=[]

        for ch in s:
            if ch=='(':
                if depth>0:
                    ans.append(ch)
                depth+=1
            
            else:
                if depth!=1:
                    ans.append(ch)
                depth-=1
        return "".join(ans)
