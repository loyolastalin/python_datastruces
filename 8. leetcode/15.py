class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        # sort the numbers
        nums.sort()
        
        n = len(nums)
        
        res = []
        
        for i in range(n):
            
            # skip the duplicate values
            # as nums[i] forms first value of the triplet
            # these duplicate values will always produce duplicates
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            lo = i + 1
            hi = n - 1
            
            while lo < hi:
                    
                total = nums[i] + nums[lo] + nums[hi]
                
                if total == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    
                    # skip values that are equal to nums[hi]
                    # as these will be duplicate results
                    val = nums[hi]
                    while hi > lo and nums[hi] == val:
                        hi -= 1
                    
                    # skip values that are equal to nums[lo]
                    # as these will be duplicate results
                    val = nums[lo]
                    while lo < hi and val == nums[lo]:
                        lo += 1
                
                elif total > 0:
                    hi -= 1
                    
                else:
                    lo += 1
                        
        return res