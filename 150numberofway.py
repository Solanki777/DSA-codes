import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=10**9 + 7
        adjlist=[[] for _ in range(n)]
        for u,v,dis in roads:
            adjlist[u].append((v,dis))
            adjlist[v].append((u,dis))
        queue=[(0,0)]
        ways=[0]*n
        ways[0]=1
        dist=[float('inf')]*n
        dist[0]=0

        while queue:
            curr_dist,curr_node=heapq.heappop(queue)

            if curr_dist>dist[curr_node]:
                continue

            for neg,wt in adjlist[curr_node]:
                new_dist=wt+curr_dist
                if dist[neg]>new_dist:
                    heapq.heappush(queue,(new_dist,neg))
                    ways[neg]=ways[curr_node]
                    dist[neg]=new_dist
                elif dist[neg]==new_dist:
                    ways[neg]=(ways[neg]+ways[curr_node])%MOD
        return ways[n-1]

    
# Time: O((V + E) log V)
# Space: O(V + E)
       