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
        
        if self.size[pu]<self.size[pv]:
            self.parent[pu]=pv
            self.size[pv]+=self.size[pu]
        else:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
            
        return True
    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # to connnect n nodes require n-1 edges
        if len(connections)<n-1:
            return -1
        com=0
        dst=Disjoint(n)



        for u,v in connections:
            dst.union(u,v)
        
        for i in range(n):
            if dst.parent[i]==i:
                com+=1

        return com-1
                
# Time: O(E · α(N)) ≈ O(E)
# Space: O(N)

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1

        adjlist=[[] for _ in range(n)]
        visited=[0]*n
        for u,v in connections:
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        def dfs(i):
            visited[i]=1
            for neb in adjlist[i]:
                if visited[neb]==0:
                    dfs(neb)
        
        com=0
        for i in range(n):
            if visited[i]==0:
                com+=1
                dfs(i)
        return com-1
    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1

        visited=[0]*n
        adjlist=[[]for _ in range(n)]
        for u,v in connections:
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
        
        for i in range(n):
            if visited[i]==0:
                bfs(i)
                city+=1
        return city-1
        

        
        
        

        

                
        

        