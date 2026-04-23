# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = vala
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr=root
        ans=float('-inf')
        
        while curr:

            if curr.left!=None:
                pred=curr.left
            
                while pred.right!=None and pred.right!=curr:
                    pred=pred.right

                if pred.right==None:
                    pred.right=curr
                    curr=curr.left

                if pred.right==curr:
                    pred.right=None
                    if curr.val<=ans:
                        return False
                    else:
                        ans=curr.val
                        
                    curr=curr.right
            
            else:
                
                if curr.val<=ans:
                        return False
                else:
                    ans=curr.val
                    
                curr=curr.right
        
        return True

# Time complexity is O(n) and space complexity is O(1) 
