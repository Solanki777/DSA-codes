# Time complexity is O(Edges + no.path * lengthofpath * edges) and space complexity is O(edges + validpaths + vertex)
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        graph={}

        if len(edges)==0:
            return -1

     
        for u, v, w in edges:
            if online[v] and online[u]:
                if u not in graph:
                    graph[u]=[]
                graph[u].append((v, w))

        goal = len(online) - 1
        all_paths = []
        temp=k

        def dfs(node, path , health):
            # Offline intermediate node
            if health<0:
                return

            path.append(node)

            if node == goal:
                all_paths.append(path[:])
            else:
                for nxt, wt in graph.get(node,[]):
                    dfs(nxt, path, health-wt)

            path.pop()

        dfs(0, [] ,temp)

        def get_weight(u, v):
            for nxt, wt in graph.get(u,[]):
                if nxt == v:
                    return wt
            return None

        ans = -1

        for path in all_paths:
            minimum = float("inf")

            for i in range(len(path) - 1):
                w = get_weight(path[i], path[i + 1])
                minimum = min(minimum, w)

            ans = max(ans, minimum)

        return ans