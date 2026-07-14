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
        