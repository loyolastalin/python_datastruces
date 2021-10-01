from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        
        # When I see a char again, I can set the start pos as
        # the next char of last occurence of this char
        
        d = defaultdict(lambda: -1)
        
        start = 0
        end = 0
        
        res = 0
        
        while end < n:
            
            start = max(start, d[s[end]] + 1)
            d[s[end]] = end
            
            res = max(res, end - start + 1)
            
            end += 1
        
        return res