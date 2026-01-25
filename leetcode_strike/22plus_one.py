class Solution:
    def get_ans(self,nums):
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<9:
                nums[i]+1
                return nums
            nums[i]==0
        # if all are 9 then answer is 001
        return nums[i]+1

nums=[1,2,3]
s=Solution()
print(s.get_ans(nums))