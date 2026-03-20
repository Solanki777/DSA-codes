class Solution:
    def longestOnes(self, nums, r):
        i=0
        j=0
        size=len(nums)
        maxi=0
        while j<size:
            if nums[j]==0:
                r-=1
            
            while r<0:
                if nums[i]==0:
                    r+=1
                i+=1

            maxi=max(maxi,j-i+1)
            j+=1
            
        return maxi

# Time complexity is O(n) and space complexity is O(n)