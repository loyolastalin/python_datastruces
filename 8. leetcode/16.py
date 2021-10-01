class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        n = len(nums)
        
        s = sum(nums[:3])
        
        for i in range(n):
            
            lo, hi = i + 1, n - 1
            
            while lo < hi:
                
                sum_ = sum([nums[i], nums[lo], nums[hi]])
                
                if sum_ == target:
                    return sum_
                
                if abs(sum_ - target) < abs(s - target):
                    s = sum_
                    
                if sum_ < target:
                    lo += 1
                
                else:
                    hi -= 1
                    
        return s