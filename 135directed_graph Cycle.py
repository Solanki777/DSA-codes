class Solution:
    def isCyclic(self, V, edges):
        adjlist=[[] for _ in range(V)]
        visted=[-1]*V
        
        def cycle(node):
            visted[node]=1
            for neg in adjlist[node]:
                if visted[neg]==-1:
                    if cycle(neg):
                        return True
                elif visted[neg]==1:
                    return True
            
            visted[node]=2            
            return False
        
        for u,v in edges:
            adjlist[u].append(v)

        for i in range(len(visted)):
            if visted[i]==-1:
                if cycle(i):
                    return True
        return False

# Time and space complexity is O(V+E)