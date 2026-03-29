'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import deque

class Solution:
    def bottomView(self, root):
        queue=deque([])
        dic=dict()
        ans=[]
        l=0
        queue.append([l,root])
        min_l=max_l=0

        while queue:
            l,node=queue.popleft()
            dic[l]=node.data

            min_l=min(min_l,l)
            max_l=max(max_l,l)
            if node.left:
                queue.append([l-1,node.left])
            if node.right:
                queue.append([l+1,node.right])
        
        for i in range(min_l,max_l+1):
            ans.append(dic[i])
        return ans 

# Time complexity is O(n) for sorting 
# and space complexity is O(n)



        