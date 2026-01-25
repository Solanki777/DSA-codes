class Solution:
    def get_ans(self,nums):
        # first sort the arry
        nums.sort()
        n=len(nums)
        i=0
        j=n-1
        ans=float("-inf")
        while i<j:
            ans=max(ans,nums[i]+nums[j])
            i+=1
            j-=1
        return ans

nums=[3,5,2,3]
# here we have to pair like first take maximum and minimum value from the array make them a pair the find maximum sum among them 
s=Solution()
print(s.get_ans(nums))