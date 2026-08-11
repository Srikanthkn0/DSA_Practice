class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        visits = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            for nei in adj[node]:
                if not visits[nei]:
                    visits[nei] = True
                    dfs(nei)

        res = 0

        for n in range(n):
            if not visits[n]:
                dfs(n)
                res += 1
        
        return res