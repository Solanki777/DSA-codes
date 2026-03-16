class Solution:
    def asteroidCollision(self, asteroids):
        stack=[]
        for el in asteroids:
            if el>0:
                stack.append(el)
            
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(el) :
                    stack.pop()
            
                if len(stack)==0 or stack[-1]<0:
                    stack.append(el)
                
                elif stack and stack[-1]==abs(el):
                    stack.pop()
        
        return stack
            
# time complexity O(2n) and space complexity is O(n)
        

sl=Solution()
sl.asteroidCollision([4,7,1,1,2,-3,-7,17,15,-18,-19])
