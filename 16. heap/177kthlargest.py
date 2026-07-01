class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
        nums.sort(reverse=True)
        return nums[k-1]
# time complexity is O(nlogn) and space complexity is O(1)

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans=[]
        n=len(nums)

        # time complexity is O(klogk)
        for i in range(k):
            heapq.heappush(ans,nums[i])
        
        # time complexity is O(n-k log k)
        for i in range(k,n):
            if nums[i]>ans[0]:
                heapq.heappop(ans)
                heapq.heappush(ans,nums[i])
        
        return ans[0]

# Time complexity is O(nlogk) and space complexity is O(1)

# You know the quick sort where the pivot becomes the exact positined character . like after first itration pivot gets the right position so we apply it here
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left=0
        right=len(nums)-1

        while True:
            pivotindx=self.findindx(left,right)
            findpos=self.quick(left,right,nums,pivotindx)
            if findpos==k-1:
                return nums[findpos]
            elif findpos<k-1:
                left=findpos+1                
            else:
                right=findpos-1
                


    
    def findindx(self,left,right):
        return random.randint(left,right)
    
    def quick(self,left,right,nums,pivotinx):
        nums[left],nums[pivotinx]=nums[pivotinx],nums[left]
        pivot=nums[left]
        ind=left+1
        for i in range(left+1,right+1):
            if nums[i]>=pivot:
                nums[ind],nums[i]=nums[i],nums[ind]
                ind+=1
        nums[ind-1],nums[left]=nums[left],nums[ind-1]
        return ind-1
    
# Time complexity is O(n) but in worst case if right moves only single digit to left side the time complexity becomes O(n^2) which can be come from lots of duplicates and space complexity is O(1)
        