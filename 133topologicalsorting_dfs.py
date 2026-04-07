
# precondition : for topological sorting there must no cycle
class Solution:
        
    def topoSort(self, V, edges):
        visited=[-1 for _ in range(V)]
        stack=[]
        def dfs(node,visited):
            stack.append(node)


        for nodes in range(len(edges)):
            if len(edges[nodes])==0:
                dfs(edges[nodes],visited)
        
        
        
        
        