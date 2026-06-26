# time complexity is O(n*3) and space complexity is O(n) 
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ok=0

        for start in range(len(nums)):
            for end in range(start,len(nums)):
                ans=nums[start:end+1]
                l=len(ans)
                must=l//2+1
                count=0

                for i in ans:
                    
                    if i==target:
                        count+=1
                if count>=must:
                    ok+=1
        return ok

# Time complexity is O(n^2) and space complexity is O(1)
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ok=0

        for start in range(len(nums)):
            count=0
            for end in range(start,len(nums)):
                if nums[end] ==target:
                    count+=1
                     
                if count>=(end-start+1)//2+1:
                    ok+=1
        return ok

