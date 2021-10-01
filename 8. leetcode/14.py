class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        done=False
        if strs==[]: return ""
        while not done:
            c=''
            for j,s in enumerate(strs):
                if i == len(s):
                    done=True
                    break
                if j==0: c=s[i]
                if c!=s[i]: 
                    done=True
                    break
            if not done: i+=1
        return strs[0][0:i]