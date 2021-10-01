class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        res = []
        
        def recurse(s, left, right):
            
            if len(s) == 2 * n:
                res.append(''.join(s))
                return
            
            if left < n:
                s.append('(')
                recurse(s, left + 1, right)
                s.pop()
            
            if right < left:
                s.append(')')
                recurse(s, left, right + 1)
                s.pop()
                
        recurse([], 0, 0)
        
        return res