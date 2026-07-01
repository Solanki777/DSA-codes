# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# usign recursion 
class Solution:
    def maxDepth(self, root):
        if root==None:
            return 0
        
        leftheight=self.maxDepth(root.left)
        rightheight=self.maxDepth(root.right)

        return 1+max(leftheight,rightheight)
    
# time complexity is O(n) and space complexity is O(h) where h is height of the tree

# using bfs traverse
# number of levels==number of hieght
from collections import deque
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        
        queue=deque([])
        queue.append(root)
        height=0

        while len(queue)!=0:
            height+=1
            trav=len(queue)

            for _ in range(trav):
                node=queue.popleft()
                if node.right!=None:
                    queue.append(node.right)
                if node.left!=None:
                    queue.append(node.left)
        return height
 
# time and space complexity is O(n)