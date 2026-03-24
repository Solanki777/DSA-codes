# Different Traversals

# 1.DFS[Depth First Search]:

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

# -preorder:(root,left,right)
class Solution:
    
    def preorder(self,node):
        if node==None:
            return
        print(node.value , end=" ")
        self.preorder(node.left)
        self.preorder(node.right)



    # -inorder:(left,root,right)
    def inorder(self,node):
        if node==None:
            return
        
        self.inorder(node.left)
        print(node.value, end=" ")
        self.inorder(node.right)
    
    # -postorder:(left,right,root)
    def postorder(self,node):
        if node==None:
            return
        
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value, end=" ")


# Create nodes
root = Node(5)

root.left = Node(3)
root.right = Node(4)

root.left.left = Node(2)
root.left.right = Node(9)

root.right.left = Node(8)
root.right.right = Node(10)

root.right.left.left = Node(1)
root.right.left.right = Node(6)

Solution().preorder(root)
Solution().inorder(root)
Solution().postorder(root)



# 2.BFS[Bredth First Search]:
# -level order Traversal
