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
        
        leftnode=self.solve(root.left)
        rightnode=self.solve(root.right)
        self.diameter=max(self.diameter,leftnode+rightnode)

        return 1+max(leftnode,rightnode)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        self.solve(root)
        
        return self.diameter
    
# time complexity is O(n) and space complexity is O(h)        