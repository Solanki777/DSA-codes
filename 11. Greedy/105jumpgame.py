class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump=0
        for i in range(len(nums)):
            if i>max_jump:
                return False
            max_jump=max(max_jump,nums[i]+i)
        return True
        
# Time complexity and space complexity is O(n)