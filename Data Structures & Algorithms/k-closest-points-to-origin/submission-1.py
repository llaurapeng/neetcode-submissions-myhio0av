class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #calculate the distance for each of the points 
        
        distances = []
        for point in points: 
            x1 = point [0] 
            y1 = point [1] 

            x2 = 0 
            y2 = 0

            distances.append ([(math.sqrt((x1 - x2)**2 + (y1 - y2)**2)), [x1,y1]])

        distances.sort()
        print (distances)
        ret = []
        for x in distances[:k]: 
            ret.append ([x[1][0], x[1][1]])

        return ret
        

