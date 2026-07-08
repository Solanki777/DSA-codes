"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
# Time complexity is O(n) and space complexity is O(1)
class Solution:
    def findFrequency(self, arr, x):
        count=0
        for i in arr:
            if i==x:
                count+=1
        return count
        # code here
        