class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution(object):
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.max_product = 0

        def totalsum(node):
            if not node:
                return 0
            return node.val + totalsum(node.left) + totalsum(node.right)

        total = totalsum(root)
        
        def postorder(node):
            if not node:
                return 0

            left_sum = postorder(node.left)
            right_sum = postorder(node.right)
            sub_sum = node.val + left_sum + right_sum

            product = sub_sum * (total - sub_sum)
            self.max_product = max(self.max_product, product)

            return sub_sum

        postorder(root)
        return self.max_product % MOD   # ✅ THIS WAS MISSING

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

sl=Solution()
print(sl.maxProduct(root))

