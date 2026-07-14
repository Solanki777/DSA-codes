# time complexity is O(3^n) and space complexity is O(n)
class Solution:
    def gcd(self , a , b):
        
        while b != 0:
            a , b = b , a % b
        return a
    
    def recursion(self ,nums , index , gcd1 ,gcd2):

        if index == len(nums):
            if gcd1 != 0 and gcd2 != 0 and gcd1 == gcd2:
                return 1
            else:
                return 0

        skip = self.recursion(nums,index+1,gcd1,gcd2)
        take1 = self.recursion(nums,index +1 , self.gcd(gcd1,nums[index]), gcd2)
        take2 = self.recursion(nums,index +1 , gcd1 , self.gcd(gcd2,nums[index]))
        return skip+take1 + take2
        

    def subsequencePairCount(self, nums: List[int]) -> int:
        return self.recursion(nums,0,0,0)


# TIme complexity and space complexity is O(n * m *m)  where m is factor for calcultaing posible values of gcd1 and gcd2 each 
class Solution:
    def gcd(self , a , b):
        
        while b != 0:
            a , b = b , a % b
        return a

    
    def recursion(self ,nums , index , gcd1 ,gcd2 ,dp):

        if (index,gcd1,gcd2) in dp:
            return dp[(index,gcd1,gcd2)]

        if index == len(nums):
            if gcd1 != 0 and gcd2 != 0 and gcd1 == gcd2:
                return 1
            else:
                return 0

        skip = self.recursion(nums,index+1,gcd1,gcd2 ,dp)
        take1 = self.recursion(nums,index +1 , self.gcd(gcd1,nums[index]), gcd2 ,dp)
        take2 = self.recursion(nums,index +1 , gcd1 , self.gcd(gcd2,nums[index]) ,dp)
        
        dp[(index,gcd1,gcd2)] = skip+take1 + take2
        return skip+take1 + take2
        

    def subsequencePairCount(self, nums: List[int]) -> int:
        dp = {}
        return self.recursion(tuple(nums),0,0,0 ,dp )% (10**9 + 7)
    
# tabulation remove the recursion
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        MAX = max(nums)

        dp = [[[0] * (MAX + 1) for _ in range(MAX + 1)]
              for _ in range(n + 1)]

        for g in range(1, MAX + 1):
            dp[n][g][g] = 1

        for index in range(n - 1, -1, -1):
            x = nums[index]

            for g1 in range(MAX + 1):
                for g2 in range(MAX + 1):

                    skip = dp[index + 1][g1][g2]

                    take1 = dp[index + 1][gcd(g1, x)][g2]

                    take2 = dp[index + 1][g1][gcd(g2, x)]

                    dp[index][g1][g2] = (skip + take1 + take2) % MOD

        return dp[0][0][0]
        