class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                lo, hi = j + 1, len(nums) - 1
                while lo < hi:
                    s = nums[lo] + nums[hi] + nums[j] + nums[i]
                    if s > target:
                        hi -= 1
                    elif s < target:
                        lo += 1
                    else:
                        res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == res[-1][2]: lo += 1
                        while lo < hi and nums[hi] == res[-1][3]: hi -= 1
        return res