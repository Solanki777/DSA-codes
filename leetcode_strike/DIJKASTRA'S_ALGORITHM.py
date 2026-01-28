# undirected graph



import heapq

def sort_path(edges,src,n):

    # build the adjacency list since undirected graph has outgoing and incoming pair with same weight so
    adj={i:[] for i in range(n)}
    for u,v,w in edges:
        # outgoing 
        adj[u].append((v,w))
        # incoming
        adj[v].append((u,w))

    print(adj)

    # build the minimum_distancearr
    dist=[float('inf')]*n

    # dist from sorce to sorce is zero
    dist[src]=0

    # build heap and insert first value also
    min_heap=[(0,src)]

    while min_heap:
        curr_dist,curr_node=heapq.heappop(min_heap)
        
        # if current distance is larger that minimum distance stored in dist then continue
        if curr_dist>dist[curr_node]:
            continue

        # now get the neighobour of curr_node from the adjacency list
        for v,w in adj[curr_node]:
            # calculate the new distance form the source to node v
            new_dist=curr_dist+w

            # if new distance is smaller than stored distance for node v then change the new distance in distance array and push that minimum distance in heap for letter use
            if new_dist<dist[v]:
                dist[v]=new_dist
                heapq.heappush(min_heap,(new_dist,v))



    return dist


edges=[[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2

print(sort_path(edges,src,3))