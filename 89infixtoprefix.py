class Solution():
    def pres(self, ch):
        if ch == '^':
            return 3
        if ch == '*' or ch == '/':
            return 2
        if ch == '+' or ch == '-':
            return 1
        return 0
    
    def inftopref(self, s):  # don't use 'str' as variable name
        # Step 1: reverse string + swap brackets
        rev = ""
        for ch in s:
            if ch == '(':
                rev = ')' + rev
            elif ch == ')':
                rev = '(' + rev
            else:
                rev = ch + rev

        stack = []
        ans = []

        # Step 2: infix to postfix (on reversed string)
        for ch in rev:
            if ch.isalnum():
                ans.append(ch)
            
            elif ch == '(':
                stack.append(ch)
            
            elif ch == ')':
                while stack and stack[-1] != '(':
                    ans.append(stack.pop())
                stack.pop()
            
            else:  # operator

                
                while stack and self.pres(stack[-1]) > self.pres(ch):
                    ans.append(stack.pop())
                stack.append(ch)
        
        while stack:
            ans.append(stack.pop())

        # Step 3: reverse postfix to get prefix
        postfix = "".join(ans)
        return postfix[::-1]


s = "F+O-C*(B+A)"
print(Solution().inftopref(s))