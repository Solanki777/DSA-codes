class Solution:
    def recursion(self,arr,sum,index,current_sum):
        if sum==current_sum:
            return True
        if index>=len(arr) or current_sum>sum:
            return False
        
        take=self.recursion(arr,sum,index+1,arr[index]+current_sum)
        nottake=self.recursion(arr,sum,index+1,current_sum)

        return take or nottake
        
    def isSubsetSum (self, arr, sum):
        return self.recursion(arr,sum,0,0)
    
# dp
class Solution:
    def recursion(self,arr,sum,index,current_sum,dp):
        if sum==current_sum:
            return True
        if index>=len(arr) or current_sum>sum:
            return False
        
        if (index,current_sum) in dp:
            return dp[(index,current_sum)]
        
        take=self.recursion(arr,sum,index+1,arr[index]+current_sum,dp)
        nottake=self.recursion(arr,sum,index+1,current_sum,dp)

        dp[(index,current_sum)]=take or nottake

        return dp[(index,current_sum)]
        
    def isSubsetSum (self, arr, sum):
        dp={}
        return self.recursion(arr,sum,0,0,dp)
        