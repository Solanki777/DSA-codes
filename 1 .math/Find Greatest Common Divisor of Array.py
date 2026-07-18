class Solution:
    def gcd(self, a ,b ):
        while b :
            a , b = b , a % b
        return a
    def findGCD(self, nums: List[int]) -> int:
        small = float('inf')
        big = float('-inf')

        for el in nums:
            small = min(small , el)
            big = max(big , el)
        
        return self.gcd(small, big)
        
# time complexity is O(n) + O(log(min(a,b))) and space complexity is O(1)