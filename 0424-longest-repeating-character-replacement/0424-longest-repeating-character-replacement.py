class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxcount=0
        maxlen=0
        freq=[0]*26
        l=0
        for r in range(len(s)):
            freq[ord(s[r])-ord('A')]+=1
            maxcount=max(maxcount,freq[ord(s[r])-ord('A')])
            while (r-l+1)-maxcount>k:
                freq[ord(s[l])-ord('A')]-=1
                l+=1
            maxlen=max(maxlen,(r-l+1))
        return maxlen


        