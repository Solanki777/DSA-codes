'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        curr=root

        # exact smallet than key 
        pred=None
        while curr:
            if curr.data<key:
                pred=curr
                curr=curr.right
            else:
                curr=curr.left
        
        succ=None
        curr=root
        while curr:
            if curr.data>key:
                succ=curr
                curr=curr.left
            else:
                curr=curr.right
        
        return pred,succ

# TIme complexity is O(N) and space complexity is O(1)