import heapq
class Solution:
    def sortes_path(self,n,m,edges):
        # 1 starting graph
        adjlist=[[] for _ in range(n+1)]
        for u,v,d in edges:
            adjlist[u].append((v,d))
            adjlist[v].append((u,d))
        
        distance=[float('inf') for _ in range(n+1)]
        distance[1]=0

        parent=[i for i in range(0,n+1)]
        priority_queue=[]
        heapq.heappush(priority_queue,((0,1)))

        while priority_queue:
            curr_dist,curr_node=heapq.heappop(priority_queue)

            if curr_dist>distance[curr_node]:
                continue

            for neg,d in adjlist[curr_node]:
                new_dist=curr_dist+d

                if new_dist<distance[neg]:
                    distance[neg]=new_dist
                    heapq.heappush(priority_queue,(new_dist,neg))
                    parent[neg]=curr_node
        
        if distance[n]==float('inf'):
            return -1
        
        path=[]
        node=n
        while parent[node]!=node:
            path.append(node)
            node=parent[node]
        path.append(1)
        return list(reversed(path))

# Time complexity is O(E log V) and space complexity is O(V+E) 


                


