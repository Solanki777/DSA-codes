import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        adjlist=[[] for _ in range(V)]

        for u,v,d in edges:
            adjlist[u].append([v,d])
            adjlist[v].append([u,d])

        distance=[ float('inf') for _ in range(V)]

        queue=[[0,src]]
        distance[src]=0

        
        while queue:

            dist,curr_node=heapq.heappop(queue)
            if dist>distance[curr_node]:
                continue

            for neg,d in adjlist[curr_node]:
                new_dist=d+dist

                if new_dist<distance[neg]:
                    distance[neg]=new_dist
                    heapq.heappush(queue,[new_dist,neg])
                
        return distance

# Time Complexity: O(E log V)
# Space Complexity: O(E + V)
        
