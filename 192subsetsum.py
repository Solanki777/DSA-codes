# time and space comlexity is O(2*n) and space compelxity is O(n)
class Solution:
    def recursion(self,arr,sum,index,curr_sum):
        if curr_sum==sum:
            return True
        if index>len(arr)-1:
            return False
        if curr_sum>sum:
            return False
     
        
        pick=self.recursion(arr,sum,index+1,curr_sum+arr[index])
        notpick=self.recursion(arr,sum,index+1,curr_sum)

        return pick or notpick
    def isSubsetSum (self, arr, sum):
        return self.recursion(arr,sum,0,0)

# intro to dp
class Solution:
    def recursion(self,arr,sum,index,curr_sum,dp):

        if (curr_sum,index) in dp:
            return dp[(curr_sum,index)]
        
        if curr_sum==sum:
            return True
        if index>len(arr)-1:
            return False
        if curr_sum>sum:
            return False
        
        pick=self.recursion(arr,sum,index+1,curr_sum+arr[index],dp)
        notpick=self.recursion(arr,sum,index+1,curr_sum,dp)

        dp[(curr_sum,index)]=pick or notpick

        return dp[(curr_sum,index)]
    def isSubsetSum (self, arr, sum):
        dp={}
        return self.recursion(arr,sum,0,0,dp)


# tablation : time and space complexity len(arr) * sum 
class Solution:
    def isSubsetSum(self,arr,sum):
        dp=[[False for _ in range(sum+1)] for _ in range(len(arr))]
        n=len(arr)
        
        for index in range(n):
            dp[index][0]=True
        
        if sum>=arr[0]:
            dp[0][arr[0]]=True
        
        for index in range(1,n):
            for  target in range(1,sum+1):
                note_take=dp[index-1][target]
                take=False

                if arr[index]<=target:
                    take=dp[index-1][target-arr[index]]
                dp[index][target]=take or note_take

        return dp[n-1][sum]

# space complexity is improved to O(sum)
class Solution:
    def isSubsetSum(self,arr,sum):
        prev=[False for _ in range(sum+1)] 
        n=len(arr)
        prev[0]=True
        
        if sum>=arr[0]:
            prev[arr[0]]=True
        
        for index in range(1,n):
            curr=[False for _ in range(sum+1)]
            curr[0]=True
            for  target in range(1,sum+1):
                note_take=prev[target]
                take=False

                if arr[index]<=target:
                    take=prev[target-arr[index]]
                curr[target]=take or note_take
            prev=curr

        return prev[sum]

       