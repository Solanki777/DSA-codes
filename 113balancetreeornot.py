# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if root is None:
            return 0
        leftheight=self.solve(root.left)
        if leftheight==-1:
            return -1
        rightheight=self.solve(root.right)
        if rightheight==-1:
            return -1
        
        if abs(leftheight-rightheight)>1:
            return -1
        return 1+max(leftheight,rightheight)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=self.solve(root)
        if ans==-1:
            return False
        return True
        
# TIme complexity is O(n) and space complexity is O(h)cP