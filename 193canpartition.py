class Solution:
    def canPartition(self,nums):
        s=[]
        arr=[]

        def recursion(nums,s,index,arr):
            if index==len(nums):
                s.append(arr.copy())
                return
            arr.append(nums[index])
            recursion(nums,s,index+1,arr)
            arr.pop()
            recursion(nums,s,index+1,arr)

        recursion(nums,s,0,arr)
        return s

arr=[5,3,2,1,0]
sl=Solution()
print(sl.canPartition(arr))