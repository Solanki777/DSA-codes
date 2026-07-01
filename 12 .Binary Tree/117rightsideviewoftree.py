# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bruteforce solutinn using dictionary and stack
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue=deque([])
        queue.append(root)
        resut=[]

        while queue:
            size=len(queue)
            for lvl in range(size):
                temp=queue.popleft()
                
                if lvl==size-1:
                    resut.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return resut
            
# now we use reverse preorder traversal(root,right,left)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.result=[]
        def solve(node,level):
            if not node:
                return 
            
            if level==len(self.result):
                self.result.append(node.val)

            if node.right:
                solve(node.right,level+1)
            if node.left:
                solve(node.left,level+1)
        
        solve(root,0)

        return self.result
                
# here we not rquire any extra space 
# time and space complexity is O(n)

        