class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited=[-1 for _ in range(len(graph))]
        def dfs(i,color):
            visited[i]=color
            for adj in graph[i]:
                if visited[adj]==-1:
                    if not dfs(adj,1-color):
                        return False 
                if visited[adj]==color:
                    return False
            return True
            
            


        for i in range(len(visited)):
            if visited[i]==-1:
                if not dfs(i,0):
                    return False
        return True

# Time complexity is O(V+E) and space complexity is O(v) in stack space 