class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        dist=[[float('inf') for _ in range(n)] for _ in range(n)]

        for u,v,w in edges:
            dist[u][v]=w
            dist[v][u]=w
        
        for i in range(n):
            dist[i][i]=0

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via]!=float('inf') and dist[via][j]!=float('inf'):
                        dist[i][j]=min(dist[i][j],dist[i][via]+dist[via][j])
        
        city=0
        min_con=n
        for i in range(n):
            count=0
            for j in range(n):
                if dist[i][j]<=distanceThreshold:
                    count+=1
            if count<=min_con:
                min_con=count
                city=i
        return city

# Time complexity is O(n^3) and space complexity is O(n^2)

# optimal solution
import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        adj=[[] for _ in range(n)]

        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        
        
        def dijkastra(src):
            dist=[float('inf')]*n
            dist[src]=0

            heap=[(0,src)]
            count=0

            while heap:
                d,node=heapq.heappop(heap)
            
                if d>dist[node]:
                    continue

                for neb,w in adj[node]:
                    new_dist=d+w
                    if new_dist<dist[neb]:
                        heapq.heappush(heap,(new_dist,neb))
                        dist[neb]=new_dist
            
            for i in range(n):
                if dist[i]<=distanceThreshold:
                    count+=1
            return count


        city=0
        conn=n
        for i in range(n):
            count=dijkastra(i)
            if count<=conn:
                city=i
                conn=count
        return city

        
        


# Time complexity is (n*E log V) and space complexity is O(V+E)
        
