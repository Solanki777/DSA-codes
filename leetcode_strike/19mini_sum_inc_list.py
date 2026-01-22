class Solution:

    # brute force solution where the time complexity is O(n ^ 3) so it even not give the solution
    # def check(self, nums):
    #     # check if array is non-decreasing
    #     for i in range(len(nums) - 1):
    #         if nums[i] > nums[i + 1]:
    #             return False
    #     return True

    # def get_list(self, nums):
    #     # if already sorted
    #     if self.check(nums):
    #         return 0

    #     count = 0

    #     # repeat until sorted
    #     while not self.check(nums):

    #         mini_sum = float('inf')
    #         ind = -1

    #         # find adjacent pair with minimum sum
    #         for i in range(len(nums) - 1):
    #             curr_sum = nums[i] + nums[i + 1]
    #             if curr_sum < mini_sum:
    #                 mini_sum = curr_sum
    #                 ind = i

    #         # merge the pair
    #         s = nums[ind] + nums[ind + 1]
    #         nums.pop(ind + 1)
    #         nums.insert(ind, s)

    #         count += 1

    #     return count
    def get_list(self,nums):


nums=[5,2,3,1]
s=Solution()
print(s.get_list(nums))
