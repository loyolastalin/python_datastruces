class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        expected = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if stack and stack[-1] == expected[c]:
                    stack.pop()
                    continue
                else:
                    return False
                
        return not stack