import heapq
from collections import defaultdict


# this solution give time limit exceede but you use stake instead it will pass
# class Solution:
#     def minimumCost(self, source, target, original, changed, cost):

#         # Build graph
#         adj = defaultdict(list)
#         for i in range(len(original)):
#             adj[original[i]].append((changed[i], cost[i]))

#         total_cost = 0

#         # For each character position
#         for i in range(len(source)):
#             src = source[i]
#             dst = target[i]

#             # Same character → no cost
#             if src == dst:
#                 continue

#             # Dijkstra:

#             # now dist is such define we can access like dist['a'] which helps here 
#             dist = defaultdict(lambda: float('inf'))

#             # for source to source traverse it is zero  in aaray
#             dist[src] = 0

#             # push the inital values in heap 
#             min_heap = [(0, src)]

#             while min_heap:
#                 curr_dist, curr_node = heapq.heappop(min_heap)

#                 if curr_dist > dist[curr_node]:
#                     continue

#                 for v, w in adj[curr_node]:
#                     new_dist = curr_dist + w
#                     if new_dist < dist[v]:
#                         dist[v] = new_dist
#                         heapq.heappush(min_heap, (new_dist, v))

#             if dist[dst] == float('inf'):
#                 return -1

#             total_cost += dist[dst]

#         return total_cost
    
from sortedcontainers import SortedSet
from collections import defaultdict

class Solution:
    def minimumCost(self, source, target, original, changed, cost):

        # first build the adjacency list
        adj=defaultdict(list)
        for i in range(len(original)):
            adj[original[i]].append((changed[i],cost[i]))

        total=0
        for i in range(len(source)):
            src=source[i]
            tr=target[i]
            
            # build dictionary that can access like a['a']
            dist=defaultdict(lambda: float('inf'))
            dist[src]=0

            st=SortedSet()
            st.add((0,src))

            while st:
                curr_dist,curr_node=st.pop(0)

                for v,w in adj[curr_node]:

                    new_dist=curr_dist+w
                    if new_dist < dist[v]:
                        if dist[v] != float('inf'):

                            st.discard((dist[v],v))
                    
                        dist[v]=new_dist
                        st.add((new_dist,v))
            
            if dist[tr]==float('inf'):
                return -1
            
            total+=dist[tr]
        return total
            




        
    






        
        
        
        # for src in range(len(source))

s=Solution()
source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]
print(s.minimumCost(source,target,original,changed,cost))