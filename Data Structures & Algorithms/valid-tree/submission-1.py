class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        
        store = [[] for i in range(n)]

        for u, v in edges:
            store[u].append(v)
            store[v].append(u)
        
        visits = set()

        def dfs(node, parent):
            if node in visits:
                return False
            
            visits.add(node)

            for nei in store[node]:
                    if nei == parent:
                        continue
                    if not dfs(nei, node):
                        return False
            return True
        
        return dfs(0, -2) and len(visits) == n