# 1. What is Spanning tree ?
# spanning tree is a tree having n node and n-1 edges and also all nodes are reachable with each other
    
# 2. minimum spanning tree[mst]:
# mst is spanning tree having minimum total wieght from the all combination of mst.

# thre are two ways of finding mst:
# 1. Prim's Algorithm
# 2. Kruskal's Algorithm

# 1. Prims Algorithm
import heapq
class Solution:
    def spanningTree(self, V, edges):

        adjlist=[[] for _ in range(V)]
        for u,v,w in edges:
            adjlist[u].append((v,w))
            adjlist[v].append((u,w))
        
        # dist,src,parent for first node thre is no parent         
        heap=[(0,0,-1)]
        visited=[0]*V

        # just for stroing the path 
        mst=[]
        Sum=0
        # code here
        while heap:
            dist,node,parent=heapq.heappop(heap)
            if visited[node]!=1:
                visited[node]=1

                if parent !=-1:
                    mst.append((parent,node))
                    Sum+=dist

                for neb,wt in adjlist[node]:
                    if visited[neb]!=1:
                        heapq.heappush(heap,(wt,neb,node))
        
        return Sum
                    
# Time complexity is O(E log V) and space complexity is O(V+E)

