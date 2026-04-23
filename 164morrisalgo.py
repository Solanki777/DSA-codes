# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr=root
        result=[]
        
        while curr:

            # case 1: current has left child 
            if curr.left!=None:

                # put predeseeor left child 
                pred=curr.left
                
                # find the right most child of pred  . Make sure that pred.right is not already connected with curr if it does that means it is loop so this gives tle and not find the right most node
                while pred.right!=None and pred.right!=curr:
                    pred=pred.right
            
                # now here it has none not curr (loop). bult the thered that connect with curr. and now move curr to left side for more traversal on left side first

                if pred.right==None:
                    pred.right=curr
                    curr=curr.left

                # if curr and pred.right is same than there is thred we have first remove the thered and put the curr into list and now go to right side 
                if pred.right==curr:
                    pred.right=None
                    result.append(curr.val)
                    curr=curr.right
            
            # case 2:  curr has no left child so it is printed and it has move through thered maded by the algorithm
            else:
                
                result.append(curr.val)
                curr=curr.right
        
        return result

