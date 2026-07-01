''' class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''

class Solution:
    def findCeil(self,root, x):
        ceil=-1
        while root:
            if root.data==x:
                return root.data

            if root.data>=x:
                ceil=root.data
                root=root.left
            else:
                root=root.right
        return ceil

# Time complexity is O(logbase2n) and space complexity is O(1)

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        flour=-1
        while root:
            if root.data==k:
                return root.data
            
            if root.data<k:
                flour=root.data
                root=root.right
            else:
                root=root.left
        return flour
            
# Time complexity is O(logbase2n) and space complexity is O(1)
                