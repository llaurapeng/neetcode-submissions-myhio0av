class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range (n)}

        for u,v in edges: 
            adj[u].append (v)
            adj [v].append (u)

        #keeps track of visited nodes
        visit = set()
        def dfs (node, prev):
            if node in visit: 
                return False
            visit.add (node)
            for neighbor in adj [node]:
                if neighbor == prev: 
                    continue
                if dfs (neighbor, node) is False:
                    return False
                #case: if prev is in visit 

            return True

        return dfs (0,-1) and len (visit) == n



