# using bfs traversal
class Solution:
    def countConnected(self, V, edges):
        visited=[0]*V
        adjlist=[[]for _ in range(V)]
        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        city=0
        
        def bfs(node):
            queue=[]
            queue.append(node)
            visited[node]=1
            while queue:
                n=queue.pop(0)
                for neb in adjlist[n]:
                    if visited[neb]==0:
                        visited[neb]=1
                        queue.append(neb)
        
        for i in range(V):
            if visited[i]==0:
                bfs(i)
                city+=1
        return city

# using dfs traversal 
class Solution:
    def countConnected(self, V, edges):
        adjlist=[[] for _ in range(V)]
        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        visited=[0]*V

        def dfs(i):
            visited[i]=1
            for neb in adjlist[i]:
                if visited[neb]==0:
                    dfs(neb)
        
        city=0
        for i in range(V):
            if visited[i]==0:
                city+=1
                dfs(i)        

        return city
    
# for dfs and bfs time complexity is O(V+E) and space complexity is O(V)

# using dis joint set 
class Disjoint:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)

    # O(α(N))    
    def ultiparent(self,node):
        if node==self.parent[node]:
            return node
        
        self.parent[node]=self.ultiparent(self.parent[node])
        return self.parent[node]

    # O(α(N))    
    def union(self,u,v):
        pu=self.ultiparent(u)
        pv=self.ultiparent(v)

        if pu==pv:
            return False
        
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
            self.size[pv]+=self.size[pu]
        else:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
            
        return True
    class Solution:
        def countConnected(self, V, edges):
            ds=Disjoint(V)
            city=0
            for i in range(V):
                if ds.parent[i]==i:
                    city+=1
            return city

# time complexity is O(α(N)) and spacec omplexity O(N)