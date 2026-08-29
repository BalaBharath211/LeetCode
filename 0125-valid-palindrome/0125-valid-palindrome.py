class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(c.lower() for c in s if c.isalnum())
        return self.palindrome(0,s)
    def palindrome(self,i,s):
        n=len(s)
        if i>=n//2:
            return True 
        if s[i]!=s[n-i-1]:
            return False
        return self.palindrome(i+1,s)
