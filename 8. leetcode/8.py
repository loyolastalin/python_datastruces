class Solution:
    def myAtoi(self, str: str) -> int:
        if not str: return 0
        n,i=len(str),0
        while i<n and str[i]==' ': i+=1
        sign=1
        if i<n and str[i]=='-': 
            sign=-1
            i+=1
        elif i<n and str[i]=='+': i+=1
        res=0
        while i<n:
            if not(str[i]>='0' and str[i]<='9'): break
            res=res*10+ord(str[i])-ord('0')
            i+=1
        res*=sign
        if res>(1<<31)-1: return (1<<31)-1
        elif res<-(1<<31): return -(1<<31)
        return res 