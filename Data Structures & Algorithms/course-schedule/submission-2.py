class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #create adjancey matrix (course: prereq)
        courses = {}

        for i in range (numCourses):
            courses [i] = []

        for course, pre in prerequisites: 
            courses [course].append (pre)

        visit = set ()

        def canTake (course):

            if course in visit: 
                return False
            if len (courses[course]) == 0: 
                return True

            visit.add (course)

            for pre in courses [course]:
                if canTake (pre) is False: 
                    return False

            visit.remove (course)
            courses [course] = []

            return True


        for i in range (numCourses):
            if not canTake (i):
                return False

        return True