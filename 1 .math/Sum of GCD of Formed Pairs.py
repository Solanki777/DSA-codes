class Solution:

    # log(M)
    def gcd(self ,a,b):
        while b > 0:
            a , b = b , a%b
        return a

    def gcdSum(self, nums: list[int]) -> int:
        maxi = nums[0]
        prefix_gcd = []

        for i in nums:
            maxi = max(maxi,i)
            prefix_gcd.append((self.gcd(maxi,i)))
        
        prefix_gcd.sort()

        i = 0
        j = len(prefix_gcd) - 1
        ans = 0

        while i < j :
            ans += self.gcd(prefix_gcd[i],prefix_gcd[j])
            i+=1
            j-=1
        
        return ans

# time complexity is O(nlogM + nlogn) and space complexity is O(n)
        
        
        
            
        