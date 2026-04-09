# using bfs 

from collections import deque

class Solution:
    def isCyclic(self, V, edges):

        # 1.adjlist build 
        adjlist=[[] for _ in range(V)]
        for u,v in edges:
            adjlist[u].append(v)
        
        # 2.indegree 
        indgree=[0]*V
        for i in adjlist:
            for el in i:
                indgree[el]+=1
        
        queue=deque()
        for i in range(len(indgree)):
            if indgree[i]==0:
                queue.append(i)
        
        while queue:
            curr_node=queue.popleft()
            for neg in adjlist[curr_node]:
                indgree[neg]-=1
                if indgree[neg]==0:
                    queue.append(neg)
        
        for i in indgree:
            if i >0:
                return True
        return False
    
# time and space complexity is O(V+E)


        