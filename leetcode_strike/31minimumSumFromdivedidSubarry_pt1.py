class Solution(object):
    def minimumCost(self, nums):
        # 1 value is complasory so take as first elemtn
        first=nums[0]

        # remaining element being sorted because we have to find sencond and third minimum
        rest=sorted(nums[1:])

        return first+rest[0]+rest[1]

        
sl=Solution()
print(sl.minimumCost([1,2,12,3]))