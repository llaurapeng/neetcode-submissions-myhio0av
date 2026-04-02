class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adj = {i:[] for i in range (n)}

        for u,v in edges: 
            adj [u].append (v)

            adj[v].append (u)

        components = []
        checked = []

        def helper (node, visit):
            if adj [node] == []:
                return 

            if node in visit: 
                return 

            visit.append (node)
            checked.append (node)

            for neighbor in adj [node]:
                helper (neighbor,visit)

            return visit

        ret = 0 
        for i in range (n):
            if i in checked: 
                continue
            else: 
                helper (i, [])
                ret+=1

        return ret

        