# time and space complexity is O(n)
class Solution:
    def frequencyCount(self, arr):
        n=len(arr)
        ans=[0]*n
        
        for i in arr:
            if i-1<=n-1:
                ans[i-1]+=1
        return ans

