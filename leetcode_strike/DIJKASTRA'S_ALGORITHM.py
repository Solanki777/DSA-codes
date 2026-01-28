# # undirected graph



# import heapq

# def sort_path(edges,src,n):

#     # build the adjacency list since undirected graph has outgoing and incoming pair with same weight so
#     adj={i:[] for i in range(n)}
#     for u,v,w in edges:
#         # outgoing 
#         adj[u].append((v,w))
#         # incoming
#         adj[v].append((u,w))

#     print(adj)

#     # build the minimum_distancearr
#     dist=[float('inf')]*n

#     # dist from sorce to sorce is zero
#     dist[src]=0

#     # build heap and insert first value also
#     min_heap=[(0,src)]

#     while min_heap:
#         curr_dist,curr_node=heapq.heappop(min_heap)
        
#         # if current distance is larger that minimum distance stored in dist then continue
#         if curr_dist>dist[curr_node]:
#             continue

#         # now get the neighobour of curr_node from the adjacency list
#         for v,w in adj[curr_node]:
#             # calculate the new distance form the source to node v
#             new_dist=curr_dist+w

#             # if new distance is smaller than stored distance for node v then change the new distance in distance array and push that minimum distance in heap for letter use
#             if new_dist<dist[v]:
#                 dist[v]=new_dist
#                 heapq.heappush(min_heap,(new_dist,v))



#     return dist

# as we know that dist array stores only optimal solution that are exites like priority quue has (0,4),(0,6) means distance 0 is 4 then 6 first we pop 4 as you know than also we process the 6 unnessesarily so we have to impove that thing by the use of set which allows such deletion but python not support so we have to install that thing


from sortedcontainers import SortedSet

def sort_path(edges,src,n):
    # first create the adjacenncy list
    adj={i:[]for i in range(n)}
    # fill it 
    for u,v,w in edges:
        # outgoing
        adj[u].append((v,w))
        # incoming
        adj[v].append((u,w))

    # build the dist 
    dist=[float("inf") ] *n

    # since the sorce to sorce is zero 
    dist[src]=0

    se=SortedSet()
    se.add((0,src))

    while se:
        curr_dist,curr_node=se.pop(0)

        for v,w in adj[curr_node]:
            new_dist=curr_dist+w
            if new_dist < dist[v]:
                if dist[v] !=float("inf"):

                    # there is some value store in dist but it is not minimum so we have to change it and also we have to remove it from the set to do not go further for that part because it alsready contains the long diatance
                    se.discard((dist[v],v))
                dist[v]=new_dist
                se.add((new_dist,v))
    return dist
edges=[[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2

print(sort_path(edges,src,3))