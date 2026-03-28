# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi=float('-inf')
    def maxPathSum(self, root) -> int:
        self.maxi=float('-inf')

        def solve(node):
            if not node:
                return 0
            
            leftsum=solve(node.left)
            if leftsum<0:
                leftsum=0
            rightsum=solve(node.right)
            if rightsum<0:
                rightsum=0

            self.maxi=max(self.maxi,leftsum+node.val+rightsum)
            
            return node.val+max(leftsum,rightsum)
        
        solve(root)
        return self.maxi


# time complexity is O(n) and space complexity is O(h)