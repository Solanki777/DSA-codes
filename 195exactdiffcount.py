#User function Template for python time complexity is O(2^n) and space complexity is O(n) recursion stack space
class Solution:
	def recursion(self,arr,target,index):
		if index==0:
			if target==0 and arr[0]==0:
				return 2
			if target==0 or arr[0]==target:
				return 1
			return 0
		
		if arr[index]>target:
			pick=0
		elif arr[index]<=target:
			pick=self.recursion(arr,target-arr[index],index-1)
		not_pick=self.recursion(arr,target,index-1)
		return pick + not_pick
	def perfectSum(self, arr, target):
		# code here
		return self.recursion(arr,target,len(arr)-1)
	
# dp solution time complexity is O(n*target) and space complexity is O(n*target) + O(target)
class Solution:
	def recursion(self,arr,target,index,dp):
		if index==0:
			if target==0 and arr[0]==0:
				return 2
			if target==0 or arr[0]==target:
				return 1
			return 0
		
		if dp[target][index]!=-1:
			return dp[target][index]
		
		if arr[index]>target:
			pick=0
		elif arr[index]<=target:
			pick=self.recursion(arr,target-arr[index],index-1,dp)

		not_pick=self.recursion(arr,target,index-1,dp)
		dp[target][index]= pick + not_pick
		return dp[target][index
					]
	def perfectSum(self, arr, target):
		dp=[[-1 for _ in range(len(arr))] for _ in range(target)]
		# code here
		return self.recursion(arr,target,len(arr)-1,dp)
	
# TABULATION time and space complexity is O(target*len(arr))
class Solution:
	def perfectSum(self, arr, target):
		
		dp=[[0 for _ in range(target+1)] for _ in range(len(arr))]
		
		if arr[0]==0:
			dp[0][0]=2
		else:
			dp[0][0]=1
		
		if arr[0]!=0 and arr[0]<=target:
			dp[0][arr[0]]=1

		for index in range(1,len(arr)):
			for total in range(target+1):
				if arr[index]>total:
					pick=0
				else:
					pick=dp[index-1][total-arr[index]]
				not_pick=dp[index-1][total]
				dp[index][total]=pick+not_pick
		return dp[len(arr)-1][target]
		

# space imrpoved
class Solution:
	def perfectSum(self, arr, target):
		
		prev=[0 for _ in range(target+1)] 
		
		if arr[0]==0:
			prev[0]=2
		else:
			prev[0]=1
		
		if arr[0]!=0 and arr[0]<=target:
			prev[arr[0]]=1

		for index in range(1,len(arr)):
			curr=[0 for _ in range(target+1)]
		
			for total in range(target+1):
				if arr[index]>total:
					pick=0
				else:
					pick=prev[total-arr[index]]
				not_pick=prev[total]
				curr[total]=pick+not_pick
			prev=curr
		return prev[target]

# space complexity to 1d arry 
class Solution:
	def perfectSum(self, arr, target):
		
		prev=[0 for _ in range(target+1)] 
		
		if arr[0]==0:
			prev[0]=2
		else:
			prev[0]=1
		
		if arr[0]!=0 and arr[0]<=target:
			prev[arr[0]]=1

		for index in range(1,len(arr)):
		
			for total in range(target,arr[index]-1,-1):
				if arr[index]>total:
					pick=0
				else:
					pick=prev[total-arr[index]]
				not_pick=prev[total]
				prev[total]=pick+not_pick
		
		return prev[target]
