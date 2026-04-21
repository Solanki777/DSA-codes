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

# 2. Krushkal's algorithm

class Disjoint:
    def __init__(self,n):
        self.size=[1]*(n+1)
        self.parent=[i for i in range(n+1)]
    
    def ultiparent(self,node):

        if self.parent[node]==node:
            return node
        
        self.parent[node]=self.ultiparent(self.parent[node])

        return self.parent[node]
    
    def union(self,u,v):
        pu=self.ultiparent(u)
        pv=self.ultiparent(v)

        if pu==pv:
            return False
        
        if self.size[pu]<self.size[pv]:
            self.parent[pu]=pv
            self.size[pv]+=self.size[pu]
        
        else:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
        
        
        return True


class Solution:
    def spanningTree(self, V, edges):
        edge=[]
        for u,v,w in edges:
            edge.append((w,u,v))
        
        edge.sort()

        mst_weight=0
        dst=Disjoint(V)
        for w,u,v in edge:
            if dst.union(u,v):
                mst_weight+=w
        
        return mst_weight




# Time complexity is O(ElogE) and space complexity is O(V+E)