# Here the node flow his distance all negbour so get the minimum distance 

# 1. if thre is n nodes than the iteration to get all nodes distance is n-1 so we have to do n-1 iteration 
#2. in each iteration find the minimum distance and stored it in the distance arry

# why n-1 iteration ?
# 1->2->3->4->5
# suppose this 5 nodes havin some distance but in starting we assume infinte in distance arry in first iteration 5 give his distace to 4 . in 2 and go on .. till n-1 iteration 1 get's the distance to 5

# how it detectes cycle?
# after n-1 iteration it still changes the distination array than there is cycle and also src node's distance reduces from 0 to negative value

class Solution:
    def bellmanFord(self, V, edges, src):
        inf=100000000

        dist=[inf]*V
        dist[src]=0

        # n-1 iteration 
        for i in range(V-1):
            for u,v,d in edges:
                # now distance is spread from zero to other node 
                if dist[u]!=inf and dist[u]+d <dist[v]:
                    dist[v]=dist[u]+d
        
        # nth iteration /
        for u,v,d in edges:
            if dist[u]!=inf and dist[u]+d<dist[v]:
                return [-1]

        return dist        
        

# Time complexity is (V−1)×E=O(VE) and space complexity is O(V)