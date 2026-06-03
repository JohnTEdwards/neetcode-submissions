class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjac = [[] for i in range(n)]
        visited = [False] * n
        for x, y in edges:
            adjac[x].append(y)
            adjac[y].append(x)

        def dfs(node):
            for i in adjac[node]:
                if not visited[i]:
                    visited[i] = True
                    dfs(i)
        
        def bfs(node):
            return
        
        disconnected = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                disconnected += 1
        return disconnected

        