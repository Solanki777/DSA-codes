# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# brute force solution 
# 1. use any of traversal than sort the result and return [2] 
# use preorder traversal 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def preor(node):
            if not node:
                return 
            ans.append(node.val)
            preor(node.left)
            preor(node.right)
        
        preor(root)
        ans.sort()
        return ans[k-1]

# it takes O(n)+O(nlogn) time and O(n) space complexity 

# 2. if i use inorder traversal it give sorted result if you know first left most elemnt which smallest then root the right 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)
        return ans[k-1]
# time complexity is O(n) and space complexity is O(n)

# 3. optimal solution 
# we use morrise algorithm till we found the element we break it
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0
        curr=root
        ans=None
        while curr :
            if count==k:
                break
            elif curr.left!=None:
                pre=curr.left

                while pre.right!=None and pre.right!=curr:
                    pre=pre.right

                if pre.right==None:
                    pre.right=curr
                    curr=curr.left

                elif pre.right==curr:
                    
                    ans=curr.val
                    pre.right=None
                    curr=curr.right
                    count+=1
            else:
                ans=curr.val
                curr=curr.right
                count+=1
        return ans

# TIme complexity is O(k)  and in worst case O(n) else space complexity is O(1)



        