from collections import deque

class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution(object):
    def maxLevelSum(self,root):
        if root is None:
            return 0
        
        queue=deque([root])
        level=1
        answer_level=1
        max_sum=float('-inf')

        while queue:
            size=len(queue)
            level_sum=0

            for _ in range(size):
                node=queue.popleft()
                level_sum+=node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum >max_sum:
                max_sum=level_sum
                answer_level=level
            level+=1

        return answer_level














# ------------------ BIG TREE EXAMPLE ------------------

# Constructing a large binary tree
#
#                 10
#               /    \
#             5        20
#           /   \     /   \
#          3     7   15    25
#        /  \         \      \
#       1    4         18     30
#
root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(20)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

root.right.left = TreeNode(15)
root.right.right = TreeNode(25)

root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(4)

root.right.left.right = TreeNode(18)
root.right.right.right = TreeNode(30)

sol=Solution()
result=sol.maxLevelSum(root)

print("Level wiht maximum sum: ", result)
