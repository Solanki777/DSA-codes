"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def minValue(self, root):
        if root.left is None:
            return root.data
        return self.minValue(root.left)
        
# Time complexity is O(logbase2) and space complexity is O(1)