class Solution:
    def reverse(self, x: int) -> int:
        r=0
        if x<0:
            sin=-1
        else:
            sin=1
        x=abs(x)
        while(x>0):
            d=x%10
            r=r*10+d
            x=x//10

        s=r*sin
        if s<-2**31 or s>(2**31-1):
            return 0
        return s
        