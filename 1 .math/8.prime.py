# time complexiyt is O(n) and space complexity is O(1)
class Solution:
    def isPrime(self, n):
        if n==1:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        return 

# time comlexity is O(sqrt(n)) and space complexity is O(1)
from math import sqrt
class Solution:
    def isPrime(self, n):
        if n==1:
            return False
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                return False
        return True

        