# pure recursion time complexity(2*len(nums)) is and space complexity (len(arr))
class Solution:
    def recursion(self,arr,s1,s2,index):
        if index>=len(arr):
            return abs(s1-s2)
        
        take1=self.recursion(arr,s1+arr[index],s2,index+1)
        take2=self.recursion(arr,s1,s2+arr[index],index+1)
        return min(take1,take2)
    
    def minDifference(self, arr):
        return self.recursion(arr,0,0,0)

# using dp + recurison time complexity and space complexity is o(n*totalsum)
class Solution:
    def recursion(self,arr,s1,s2,index,dp):
        if index>=len(arr):
            return abs(s1-s2)
        if dp[index][s1]!=-1:
            return dp[index][s1]
        
        take1=self.recursion(arr,s1+arr[index],s2,index+1,dp)
        take2=self.recursion(arr,s1,s2+arr[index],index+1,dp)
        dp[index][s1]= min(take1,take2)
        return dp[index][s1]
    
    def minDifference(self, arr):
        total=sum(arr)
        dp=[[-1 for _ in range(total+1)] for _ in range(len(arr))]
        return self.recursion(arr,0,0,0,dp)
