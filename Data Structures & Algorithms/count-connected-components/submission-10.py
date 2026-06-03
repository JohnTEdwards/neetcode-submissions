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
            d = deque([node])
            visited[node] = True
            while d:
                curr = d.popleft()
                for nei in adjac[curr]:
                    if not visited[nei]:
                        visited[nei] = True
                        d.append(nei)

        
        disconnected = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                disconnected += 1
        return disconnected

        