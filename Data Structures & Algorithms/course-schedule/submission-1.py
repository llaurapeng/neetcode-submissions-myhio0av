class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create adjacency list

        adj = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites: 
            adj[course].append (pre)

        seen = set ()

        def dfs(course):
            if course in seen: 
                return False

            if adj[course] == []:
                return True

            seen.add (course)
            for pre in adj [course]:
                if not dfs (pre):
                    return False

            seen.remove (course)
            adj[course] = []
            return True

        for c in range (numCourses):
            if not dfs (c):
                return False

        return True


