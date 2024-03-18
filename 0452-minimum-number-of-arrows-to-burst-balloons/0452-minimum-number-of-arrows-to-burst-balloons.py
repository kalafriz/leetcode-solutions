class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # METHOD:
        # 1. sort
        # 2. iterate along x
        #   -> shoot when more balloons at x_i than next step x_i+1
        
        result = 0
        
        points.sort()
        print(points)
        min_end = points[0][1]
        
        for [start, end] in points:

            #print(min_end)
            
            # shoot
            if min_end < start:
                #print("shot!")
                result +=1
                min_end = end
                
            else:
                min_end = min(min_end, end)
                
        return result + 1