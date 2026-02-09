class Solution:
	def solve(self,arr,total,result,index):
		if index==len(arr):
			result.append(total)
			return 
		
		self.solve(arr,total+arr[index],result,index+1)
		self.solve(arr,total,result,index+1)

	def subsetSums(self, arr):
		result=[]
		self.solve(arr,0,result,0)
		return result
		
print(Solution().subsetSums([5,9,3]))

space complexity is O(n) like if you see recursion tree there is n depth  so space complexity is O(n) and  time complexity is O(2^n)