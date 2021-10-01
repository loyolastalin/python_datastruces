class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # you can remove the lesser of the first and the last 
        # container
        
        n = len(height)
        
        res = 0
        
        lo = 0
        hi = n - 1
        
        while lo < hi:
            
            res = max(res, min(height[lo], height[hi]) * (hi - lo))
            
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
                
        return res