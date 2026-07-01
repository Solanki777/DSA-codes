# time complexity is O(n) and space complexity is O(divisor)
class Solution:
    def getDivisors(self, n):
        ans=[]
        for i in range(1,n+1):
            if n%i==0:
                ans.append(i)
        return ans
    
from math import sqrt
class Solution:
    def getDivisors(self, n):
        ans=[]
        for i in range(1,int(sqrt(n))+1):
            if n%i==0:
                ans.append(i)
                if n//i != i :
                    ans.append(n//i)
        ans.sort()
        return ans
    
# time complexity is O(sqrt(n)) and space complexity is O(1)
    

        