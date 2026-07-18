
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


# Let:

# n=len(nums)
# q=len(queries)
# m=max(nums)

class Solution:
    def binarysearch( self, i ,j ,nums , el):
        ans = 0
        while i <= j:
            mid = i + (j - i ) //2

            if nums[mid] > el :
                ans = mid
                j = mid -1
            else:
                
                i = mid + 1
                

        return ans

    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m = max(nums)
        facto = [0] *(m+1)
        
        # O(n) 
        for x in nums:
            facto[x] += 1

        # get all divisivles O(m log m)
        for i in range(1,m+1):
            for j in range(i*2,m+1,i):
                facto[i] += facto[j]

        # getting pairs O(m)
        for i in range(1,m+1):
            pairs = int (( facto[i] * (facto[i] -1)) // 2)
            facto[i] = pairs
        
        # remove duplicates O(m log m)
        for i in range(m,0,-1):
            for j in range(i*2 , m +1 , i ):
                facto[i] -= facto[j]
        
        #cummulative sum O(m)
        for i in range(1,m+1):
            facto[i] += facto [i-1]

        # binary search O(q log m)
        res = []
        for q in queries:
            t = self.binarysearch(0,m+1,facto,q)
            res.append(t)
        
        return res

# Time complexity is O(q + mlog m + q log m) and space complexity is O(m)
        


                
        