# using recursion 
# Time complexity is (2^n) and space complexity is O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def recu(index):
            if index==len(nums)-1:
                return nums[-1]
            if index>len(nums)-1:
                return 0
            
            npick=recu(index+1)
            pick=nums[index]+recu(index+2)
            return max(npick,pick)
        return recu(0)

# use dp  space and time complexity is O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:

        dp=[-1]*len(nums)

        def recu(index):
            
            
            if index==len(nums)-1:
                return nums[-1]
            if index>len(nums)-1:
                return 0
            
            if dp[index]!=-1:
                return dp[index]
            
            npick=recu(index+1)
            pick=nums[index]+recu(index+2)
            dp[index]=max(npick,pick)
            return dp[index]
        return recu(0)

# with dp no recursion we only require previous 2 values so we can optimize this
class Solution:
    def rob(self, nums: List[int]) -> int:

        prev2=0
        prev1=nums[0]
        for index in range(1,len(nums)):
            if index>1:
                pick=nums[index]+prev2
            else:
                pick=nums[index]
            
            notpick=prev1
            curr=max(pick,notpick)
            prev2=prev1
            prev1=curr
        return prev1

# here time complexity is O(n) and space complexity is O(1)