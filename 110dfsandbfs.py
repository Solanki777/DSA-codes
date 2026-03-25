# Different Traversals

# 1.DFS[Depth First Search]:

# class Node:
#     def __init__(self, val):
#         self.value = val
#         self.left = None
#         self.right = None

# # -preorder:(root,left,right)
# class Solution:
    
#     def preorder(self,node):
#         if node==None:
#             return
#         print(node.value , end=" ")
#         self.preorder(node.left)
#         self.preorder(node.right)



#     # -inorder:(left,root,right)
#     def inorder(self,node):
#         if node==None:
#             return
        
#         self.inorder(node.left)
#         print(node.value, end=" ")
#         self.inorder(node.right)
    
#     # -postorder:(left,right,root)
#     def postorder(self,node):
#         if node==None:
#             return
        
#         self.postorder(node.left)
#         self.postorder(node.right)
#         print(node.value, end=" ")


# # Create nodes
# root = Node(5)

# root.left = Node(3)
# root.right = Node(4)

# root.left.left = Node(2)
# root.left.right = Node(9)

# root.right.left = Node(8)
# root.right.right = Node(10)

# root.right.left.left = Node(1)
# root.right.left.right = Node(6)

# Solution().preorder(root)
# Solution().inorder(root)
# Solution().postorder(root)



# 2.BFS[Bredth First Search]:
class Node:
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None
class Solution:
    def level_roder(self,node):
        result=[]
        queue=[]
        queue.append(node)

        while len(queue)!=0:
            e=queue.pop(0)
            result.append(e.value)

            if e.left !=None:
                queue.append(e.left)
            
            if e.right!=None:
                queue.append(e.right)
        
        return result

# all are O(1) operations
# time complexity is O(n) and space complexity is O(N){not exactly}


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

root.right.left.left = Node(8)
root.right.left.right = Node(9)

print(Solution().level_roder(root))




# -level order Traversal
