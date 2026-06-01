# time complexity is O(2*n) and space complexity O(n)
class Solution:
    def recursion(self,nums,index,curr,s):
        if curr==s:
            return True
        if curr>s or index>=len(nums):
            return False
        
        inlcude=self.recursion(nums,index+1,curr+nums[index],s)
        
        not_inlcude=self.recursion(nums,index+1,curr,s)

        return inlcude or not_inlcude

    def canPartition(self,nums):
        s=sum(nums)
        if s%2!=0:
            return False
        s=s/2
        return self.recursion(nums,0,0,s)

