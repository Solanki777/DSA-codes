# Time complexity is O(Edges + no.path * lengthofpath * edges) and space complexity is O(edges + validpaths + vertex)
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        graph={}

        if len(edges)==0:
            return -1

     
        for u, v, w in edges:
            if online[v] and online[u]:
                if u not in graph:
                    graph[u]=[]
                graph[u].append((v, w))

        goal = len(online) - 1
        all_paths = []
        temp=k

        def dfs(node, path , health):
            # Offline intermediate node
            if health<0:
                return

            path.append(node)

            if node == goal:
                all_paths.append(path[:])
            else:
                for nxt, wt in graph.get(node,[]):
                    dfs(nxt, path, health-wt)

            path.pop()

        dfs(0, [] ,temp)

        def get_weight(u, v):
            for nxt, wt in graph.get(u,[]):
                if nxt == v:
                    return wt
            return None

        ans = -1

        for path in all_paths:
            minimum = float("inf")

            for i in range(len(path) - 1):
                w = get_weight(path[i], path[i + 1])
                minimum = min(minimum, w)

            ans = max(ans, minimum)

        return ans


# Time complexity is O(ElogVlogW) binary + dijkastra and space complexity is O(V+E)
import heapq
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        if len(edges)==0:
            return -1

        nodes=len(online)
        adjlist=[[] for _ in range(nodes)]
        for u,v,w in edges:
            if online[u] and online[v]:
                adjlist[u].append((v,w))
    


         # find l and r
        l=float('inf')
        r=float('-inf')
        for u,v,w in edges:
            l=min(l,w)
            r=max(r,w)

        def dijkastr(minedge):

            dist=[float('inf')] * nodes
            dist[0]=0
            pq=[(0,0)]

            while pq:
                cost,node = heapq.heappop(pq)

                if cost > dist[node]:
                    continue
                
                for neg , wt in adjlist[node]:

                    if wt< minedge:
                        continue
                    
                    new_cost=cost+wt

                    if new_cost < dist[neg]:
                        dist[neg]=new_cost
                        heapq.heappush(pq, (new_cost , neg))
            
            return dist[nodes-1]<=k
                 
        # binary search
        ans=-1
        while l<=r:
            mid=int((l+r)//2)

            if dijkastr(mid):
                l=mid+1
                ans=mid
            else:
                r=mid-1

        return ans
        
                

        