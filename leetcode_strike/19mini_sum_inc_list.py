# class Solution:

#     # brute force solution where the time complexity is O(n ^ 3) so it even not give the solution
#     def check(self, nums):
#         # check if array is non-decreasing
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 return False
#         return True

#     def get_list(self, nums):
#         # if already sorted
#         if self.check(nums):
#             return 0

#         count = 0

#         # repeat until sorted
#         while not self.check(nums):

#             mini_sum = float('inf')
#             ind = -1

#             # find adjacent pair with minimum sum
#             for i in range(len(nums) - 1):
#                 curr_sum = nums[i] + nums[i + 1]
#                 if curr_sum < mini_sum:
#                     mini_sum = curr_sum
#                     ind = i

#             # merge the pair
#             s = nums[ind] + nums[ind + 1]
#             nums.pop(ind + 1)
#             nums.insert(ind, s)

#             count += 1

#         return count
    
# optimal solution
from sortedcontainers import SortedList

class Solution:
    def minimumPairRemoval(self, nums):

        # make a dubly linked list
        n = len(nums)
        prev = []
        next = []

        for i in range(n):
            prev.append(i - 1)
            next.append(i + 1)

        # set to store only sorted order sum with index (like C++ set)
        bad_pair = 0
        store_sum = SortedList()
        operation = 0

        for i in range(n - 1):

            # now we have to count the bad pair or not
            if nums[i] > nums[i + 1]:
                bad_pair += 1

            store_sum.add((nums[i] + nums[i + 1], i))

        while bad_pair != 0:

            # get minimum sum pair index
            _, curr_ind = store_sum[0]

            next_ind = next[curr_ind]
            prev_ind = prev[curr_ind]
            next_next_ind = next[next_ind]

            # if current is bad then we take a right pair so bad pari -1
            if nums[curr_ind] > nums[next_ind]:
                bad_pair -= 1

            # after making the sum the relation with previous my good_pair or bad_pair
            if prev_ind >= 0:
                # first it is bad pair then it becomes good one
                if nums[curr_ind] < nums[prev_ind] and nums[prev_ind] <= nums[curr_ind] + nums[next_ind]:
                    bad_pair -= 1

                # if it is good pair than it becomes bad
                elif nums[curr_ind] >= nums[prev_ind] and nums[prev_ind] > nums[curr_ind] + nums[next_ind]:
                    bad_pair += 1

            # now check the relation with next as same as above
            if next_next_ind < n:

                # first it is good one then it becomes bad_pair
                if nums[next_next_ind] >= nums[next_ind] and nums[next_next_ind] < nums[curr_ind] + nums[next_ind]:
                    bad_pair += 1

                # first it is bad than it becomes good one
                elif nums[next_next_ind] < nums[next_ind] and nums[next_next_ind] >= nums[curr_ind] + nums[next_ind]:
                    bad_pair -= 1

            # now merge the array so wrong value from the set
            store_sum.pop(0)

            # deleting prev then insert new data for prev sum
            if prev_ind >= 0:
                store_sum.discard((nums[prev_ind] + nums[curr_ind], prev_ind))
                store_sum.add((nums[prev_ind] + nums[curr_ind] + nums[next_ind], prev_ind))

            # for next as same
            if next_next_ind < n:
                store_sum.discard((nums[next_ind] + nums[next_next_ind], next_ind))
                store_sum.add((nums[curr_ind] + nums[next_ind] + nums[next_next_ind], curr_ind))

                # change next_next pointer
                prev[next_next_ind] = curr_ind

            # put our sum in new array
            next[curr_ind] = next_next_ind
            nums[curr_ind] = nums[curr_ind] + nums[next_ind]
            operation += 1

        return operation

nums=[10,6,5,3,7]
s=Solution()
print(s.minimumPairRemoval(nums))
