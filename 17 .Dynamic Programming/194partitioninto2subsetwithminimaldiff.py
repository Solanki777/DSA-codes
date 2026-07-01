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

# tabulation time and space complexity is O(n*total)
class Solution:
    def minDifference(self,arr):
        total=sum(arr)
        dp=[[False for _ in range(total+1)] for _ in range(len(arr))]
        

        for i in range(len(arr)):
            dp[i][0]=True
        
        dp[0][arr[0]]=True

        for i in range(1,total+1):
            for j in range(1,len(arr)):
                take=False
                not_take=dp[j-1][i]
                if arr[j]<=i:
                    take=dp[j-1][i-arr[j]]
                dp[j][i]=take or not_take
        
        # we just require last row
        min_diff=float('inf')
        for s1 in range(total+1):
            if dp[len(arr)-1][s1]==True:
                s2=total-s1
                curr_diff=abs(s2-s1)
                min_diff=min(curr_diff,min_diff)
        return min_diff

# space complexity is improved o(total)
class Solution:
    def minDifference(self,arr):
        total=sum(arr)
        prev=[False for _ in range(total+1)]
        

        prev[0]=True
        
        prev[arr[0]]=True

        for i in range(1,len(arr)):
            curr=[False for _ in range(total+1)]
            curr[0]=True
            for j in range(1,total+1):
                take=False
                not_take=prev[j]
                if arr[i]<=j:
                    take=prev[j-arr[i]]
                curr[j]=take or not_take
            
            

            prev=curr
        
        # we just require last row
        min_diff=float('inf')
        for s1 in range(total+1):
            if prev[s1]==True:
                s2=total-s1
                curr_diff=abs(s2-s1)
                min_diff=min(curr_diff,min_diff)
        return min_diff
    
# still it give tle because every time we creates new arr curr so to solve we have to done in one arr
class Solution:
    def minDifference(self,arr):
        total=sum(arr)
        dp=[False for _ in range(total+1)]
        

        dp[0]=True
        

        for num in arr:
            for s in range(total,num-1,-1):
                dp[s]=dp[s] or dp[s-num]     
        
        # we just require last row
        min_diff=float('inf')
        for s1 in range(total//2+1):
            if dp[s1]==True:
                s2=total-s1
                curr_diff=abs(s2-s1)
                min_diff=min(curr_diff,min_diff)
        return min_diff