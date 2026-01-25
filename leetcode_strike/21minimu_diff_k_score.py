class Solution:
    def minimumDifference(self, nums, k):
        # if there is only one number then return 0
        if len(nums)==1:
            return 0
        # sort the number
        nums.sort()

        # making pairs for maximum and minimum values with index diffrence of k
        i=0
        j=k-1
        ans=float("inf")
        if 1<=len(nums)<=1000:
            while j<=len(nums)-1:
                if 0<=nums[j]<=10**5:
                    ans=min(ans,nums[j]-nums[i])
                    j+=1
                    i+=1
        return ans


nums=[9,4,1,7]
s=Solution()
print(s.minimumDifference(nums,2))

        