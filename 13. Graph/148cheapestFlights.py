from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adjlist=[[] for _ in range(n)]

        for u,v,d in flights:
            adjlist[u].append((v,d))
        
        distanc=[float('inf')]*n
        queue=deque()
        queue.append((src,0,0))

        while queue :
            node,stop,cost=queue.popleft()

            if stop>k:
                break

            for neb,dis in adjlist[node]:
                if distanc[neb]>cost+dis:
                    queue.append((neb,stop+1,cost+dis))
                    distanc[neb]=cost+dis
        return -1 if distanc[dst]==float('inf') else distanc[dst]

# time complexity is O(K*E) and space complexity is O(V+E)