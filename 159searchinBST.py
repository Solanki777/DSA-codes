# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root==None:
            return
        if root.val==val:
            return root
        if root.val<val:
            self.searchBST(root.right,val)
        else:
            self.searchBST(root.left,val)

# TIme complexity is O(logbase2N) and space complexity is O(1)

from collections import deque
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp= deque()
        temp.append(root)

        while temp:
            node=temp.popleft()

            if node==None:
                continue

            if node.val==val:
                return node
            
            elif node.val<val:
                temp.append(node.right)

            else:
                temp.append(node.left)   
        return None 
        