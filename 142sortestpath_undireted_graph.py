from collections import deque
class Solution:
    def shortestPath(self, V, edges, src):
        visited=[-1]*V
        adjlist=[[] for _ in range(V)]

        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u) 
        
        dist=[-1]*V
        dist[src]=0
        visited[src]=1
        queue=deque()
        queue.append(src)

        while queue:
            node=queue.popleft()
            for neg in adjlist[node]:
                if visited[neg]==-1:
                    visited[neg]=1
                    queue.append(neg)
                    dist[neg]=dist[node]+1
        return dist
    
# TIme and space complexity is O(V+E)