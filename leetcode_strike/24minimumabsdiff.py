class Solution:
    def minimumAbsDifference(self, arr):
        # sort the arr
        arr.sort()
        mini_diff=float("inf")
        for i in range(1,len(arr)):

            # fidn the each diffrence
            diff=arr[i]-arr[i-1]
           
        #    if you found new diff which is minimum the restart the ans 
            if diff< mini_diff:
                ans=[[arr[i-1],arr[i]]]
                mini_diff=diff
            
            # if deffrence is same as mini then append another pair
            elif diff==mini_diff:
                ans.append([arr[i-1],arr[i]])
        return ans

nums=[1,10,5,6,10,11,12,7,8,0]
s=Solution()
print(s.minimumAbsDifference(nums))