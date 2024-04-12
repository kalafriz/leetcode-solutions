class Solution:
    def trap(self, height: List[int]) -> int:
        
        # METHOD: Mathematical analysis (?)
        
        # Water will spill out of its local container from the lower
        # of its two "walls"
        
        # Water will be retained from the left by the highest wall to the left
        # of the container. If there is overflow over the wall of the container,
        # it can only be retained by a higher container. Thus the water will be retained
        # from the left by the highest wall left of the current spot.
        # Same logic with right wall retaining.
        
        # Thus, water retained at current spot is only as much as the lower of its two walls,
        # which are defined by the maximum on either side
        
        
        left, right = 0, 0
        total = 0
        for i in range(1, len(height)-1):
            
            left = max(height[:i])
            right = max(height[i+1:])
            
            s = min(left, right) - height[i]
            total += s if s>0 else 0
            #print(i, ": ",left, right, s, total)
        
        return total