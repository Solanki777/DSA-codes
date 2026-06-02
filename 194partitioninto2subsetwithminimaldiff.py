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


		