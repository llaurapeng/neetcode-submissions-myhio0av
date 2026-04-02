class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        1. no cycle or loops
        2. every node is connected
        --> count of visited node is equal to the number of edges
        '''
        if len(edges) > (n - 1):
            return False
        cycle = set ()
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei in visit:
                    continue
                if not dfs(nei):
                    return False
            return True
        
        return dfs(0) and len(visit) == n
     
        