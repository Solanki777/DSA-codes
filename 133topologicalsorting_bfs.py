
# precondition : for topological sorting there must no cycle
from collections import deque
class Solution:
        
    def topoSort(self, V, edges):
        adjlist=[[] for _ in range(V)]
        indgree=[0]*V
        queue=deque()
        result=[]
        
        for u,v in edges:
            adjlist[u].append(v)
            indgree[v]+=1
        
        for i in range(V):
            if indgree[i]==0:
                queue.append(i)
        
        while queue:
            node=queue.popleft()
            result.append(node)

            for neg in adjlist[node]:
                indgree[neg]-=1
                if indgree[neg]==0:
                    queue.append(neg)
        return result



        
        
        