'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def topView(self, root):
        queue=deque([[0,root]])
        result=dict()
        ans=[]
        
        while queue:
            line,node=queue.popleft()

            if line not in result:
                result[line]=node.data

            if node.left!=None:
                queue.append([line-1,node.left])

            if node.right!=None:
                queue.append([line+1,node.right])
        for x in sorted(result):
            ans.append(result[x])
        return ans

# time complexity is O(nlogn) sorting dictionary and space complexity is O(n)
        
        