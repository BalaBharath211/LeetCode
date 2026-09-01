class Solution:
    def isPalindrome(self, x: int) -> bool:
        dup=x
        remove=0
        while x>0:
            iD=x%10
            remove=(remove*10)+iD
            x//=10
        return dup==remove


        