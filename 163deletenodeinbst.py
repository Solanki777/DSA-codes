# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        curr=root
        parent=None

        while curr and curr.val!=key:
            parent=curr
            if key<curr.val:
                curr=curr.left

            else:
                curr=curr.right
        
        # key not found 
        if not curr:
            return root
        
        def deletion(node):
            
            # case 1 empty
            if node.left==None and node.right==None:
                return None
            
            # case 2 : 1 child
            if node.left==None:
                return node.right
            elif node.right==None:
                return node.left
            
            
            # case 3 : 2 childe
            right_sub=node.right
            temp=node.left
            while temp.right:
                temp=temp.right
                
            temp.right=right_sub

            return node.left
        
        # if root is the key 
        if parent==None:
            return deletion(curr)
        
        # key is on right side 
        if parent.right==curr:
            parent.right=deletion(curr)
        
        # key is on left side 
        else :
            parent.left=deletion(curr)
        
        return root
