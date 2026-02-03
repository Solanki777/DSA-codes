
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        # define the low and high 
        low=0
        high=len(letters)-1

        # predefined ans as first iindex so we return at last 
        ans=letters[0]

        # binary search 
        while high>=low:
            mid=(low+high)//2

            if letters[mid]>target:
                high=mid-1
                ans=letters[mid]
            else:
                low=mid+1
        return ans


letters = ["c","f","j"]
target = "a"
s1=Solution()
print(s1.nextGreatestLetter(letters,target,))