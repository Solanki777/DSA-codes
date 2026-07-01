class Solution:    
    def dijkstra(self, V, edges, src):
        adjlist=[[] for _ in range(V)]
        distance=[float('inf') for _ in range(V)]

        for u,v,d in edges:
            adjlist[u].append((v,d))
            adjlist[v].append((u,d))
        
        s=set()
        s.add((0,src))
        distance[src]=0

        while s:
            curr_dist,curr_node=min(s)
            s.remove((curr_dist,curr_node))

            for neg,d in adjlist[curr_node]:
                new_dist=curr_dist+d
                if new_dist<distance[neg]:

                    # remove unwanted nodes from the set
                    if distance[neg]!=float('inf'):
                        s.discard((distance[neg],neg))
                    distance[neg]=new_dist
                    s.add((new_dist,neg))
        return distance

# time complexity is O(V^2) sorting set to get minimul distance node and space complexity is O(V+E) so that's why here we use heap insted of set 