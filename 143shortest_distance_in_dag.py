# #User function Template for python3
# 1. here since the acyclic graph is used so we use toposort so there we can get node parent before chicld
# 2. then we tranversa the toposort and find the minimum distanc and put it in answer

from typing import List


class Solution:

    # since there is no cycle so we no need for that kind of if else conditions 
    def dfs(self,node,adjlist,visited,stack):
        visited[node]=1
        for neg,dist in adjlist[node]:
            if visited[neg]==-1:
                self.dfs(neg,adjlist,visited,stack)
        
        stack.append(node)

            


    def shortestPath(self, V: int, E: int,edges: List[List[int]]) -> List[int]:
        
        adjlist=[[] for _ in range(V)]

        for u,v,d in edges:
            adjlist[u].append([v,d])
        
        # toposort using dfs
        stack=[]
        visited=[-1]*V
        for i in range(V):
            if visited[i]==-1:
                self.dfs(i,adjlist,visited,stack)
        
        distance=[float('inf') for _ in range(V)]
        distance[0]=0

        while stack:
            node=stack.pop()
            curr_dist=distance[node]
            for neg,d in adjlist[node]:
                new_dist=curr_dist+d

                if distance[neg]>new_dist:
                    distance[neg]=new_dist
        
        for i in range(V):
            if distance[i]==float('inf'):
                distance[i]=-1
        
        return distance

# Time and space complexity O(V+E)
          