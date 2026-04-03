from collections import deque

class Solution:
    def isCycle(self, V, edges):
        adj_list = [[] for _ in range(V)]
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [0] * V
        
        for i in range(V):   # handle disconnected graph
            if not visited[i]:
                queue = deque()
                queue.append((i, -1))
                visited[i] = 1
                
                while queue:
                    curr_node, parent = queue.popleft()
                    
                    for child in adj_list[curr_node]:
                        if not visited[child]:
                            visited[child] = 1
                            queue.append((child, curr_node))
                        elif child != parent:
                            return True
        
        return False

# using dfs
class Solution:
    def isCycle(self,V,edges):
        visited=[0]*V
        adj_list=[[] for _ in range(V)]

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(node,parent):
            visited[node]=1
            for new in adj_list[node]:
                if not visited[new]:
                    if dfs(new,node):
                        return True
                elif new!=parent:
                    return True
                
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i,-1):
                    return True
        return False
                