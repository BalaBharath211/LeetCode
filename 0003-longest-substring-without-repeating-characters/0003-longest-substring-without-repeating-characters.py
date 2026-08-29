class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        Hash = [-1]*256
        l,r,max_l=0,0,0
        while r<n:
            if Hash[ord(s[r])]!=-1:
                l=max(Hash[ord(s[r])]+1,l)
            cur_l=r-l+1
            max_l=max(cur_l,max_l)
            Hash[ord(s[r])]=r
            r+=1
        return max_l
