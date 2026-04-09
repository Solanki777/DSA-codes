# if tell do topological sorting using bfs than it is kahn's algorithm :

# 1. count each one of indegree
# 2. take nodes having indgree with 0 and push it into the queue
# 3.pop the node from the queue and minus the indgree of neg becuase we delete curr node
# 4.if answer length is not equal to V than there is cycle topo sort is not possible

from collections import deque
class Solution:
    def topoSort(self, V, edges):
        indegree=[0]*V
        queue=deque()
        result=[]
        adjlist=[[] for _ in range(V)]

        for u,v in edges:
            adjlist[u].append(v)
        
        for i in adjlist:
            for el in i:
                indegree[el]+=1
        
        for j in range(len(indegree)):
            if indegree[j]==0:
                queue.append(j)
            
        while queue:
            curr_node=queue.popleft()
            result.append(curr_node)

            for neg in adjlist[curr_node]:
                indegree[neg]-=1
                if indegree[neg]==0:
                    queue.append(neg)
        
        if len(result)!=V:
            return False
        return result

        
        

# time and space complexity is O(V+E)
       
        