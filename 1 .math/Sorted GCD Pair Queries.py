
class Solution:
    def gcd(self, a , b):
        while b:
            a ,b = b , a % b
        
        return a
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        gcd_pairs = []

        # O(n^2)
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if i == j :
                    continue
                else:
                    # O(logM)
                    gcd_pairs.append(self.gcd(nums[i],nums[j]))
        
        # O(logn)
        gcd_pairs.sort()
        res = []
        
        # O(n)
        for i in queries:
            if i< len(gcd_pairs):
                res.append(gcd_pairs[i])
        return res

# Time complexity is O(n^2logn) and space complexity is O(n^2) for pairs +O(q) answers
        


                
        