
# time complexity and space complexity is  O(n) 
class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        d=[0 for _ in range(len(nums))]
        for el in range(len(nums)):
            maxi=float('-inf')
            mini=float('inf')

            for digit in str(nums[el]):
                maxi=max(maxi,int(digit))
                mini=min(mini,int(digit))

            d[el]=(maxi,mini)

        digit_range=[]
        ans=0
        for maxi,mini in d:
            digit_range.append(maxi-mini)
            ans=max(ans,maxi-mini)
            
        temp=0

        for i in range(len(digit_range)):
            if digit_range[i]==ans:
                temp+=nums[i]

        return temp
