class Solution:
    def reverse(self, x: int) -> int:
        res=0
        if x==0 or x>2**31-1 or x<-(2**31): return 0
        sign=x//abs(x)
        x=abs(x)
        while x>0:
            res=res*10+x%10
            x=x//10
        if res>2**31-1 or res<-(2**31): return 0
        return sign*res