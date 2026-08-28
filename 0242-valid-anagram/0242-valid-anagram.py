class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=list(s)
        n=list(t)
        m.sort()
        n.sort()

        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            if m[i]!=n[i]:
                return False
        return True
        