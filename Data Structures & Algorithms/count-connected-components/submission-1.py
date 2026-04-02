class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adj = {i:[] for i in range (n)}

        for u,v in edges: 
            adj [u].append (v)

            adj[v].append (u)

        components = []
        checked = []

        def helper (node):
            if adj [node] == []:
                return 

            if node in checked: 
                return 

            checked.append (node)

            for neighbor in adj [node]:
                helper (neighbor)

            return 

        ret = 0 
        for i in range (n):
            if i in checked: 
                continue
            else: 
                helper (i)
                ret+=1

        return ret

        