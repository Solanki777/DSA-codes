# What is complete Binary tree:
# A tree having 2 childread except the leaf node. leaf node has 0.

# what is Almost complete binary tree
# all node should have 2 childrean except the 2nd last level and last level.Also all leaf node start from the keft side

# max heap is special type of binary tree where the parent is grater or equal to its childrean


#         50
#        /  \
#      30    40
#     / \   /
#   10 20 35


# in heap : the node values are stored in like this order 

# 50,30,40,10,20,35


# in vice versa in min heap  parent node is less than or equal to its childrean it uses almost complete binary tree because if you what to add node here then it add from left to right in the tree 


#         10
#        /  \
#      20    15
#     / \   /
#   30 40 25


# why max heap used for almost complete binary tree because it's easy to calculate this things'

# 1. you want to find the left child of the node using it's index is like: 2i+1
# 2. for right child 2i+2
# 3. if you want to find the parent (i-1)//2


# what is the internal node ?
# in case of complete binary tree total nodes are =7 and leaf node are=4 then internal nodes are =leafnode - 1 or totalnode-leafnode

# the leaf node index goes from n/2 to n-1 in 0 based indexing almost complete binary tree

# internal nodes = 0 to n/2-1    