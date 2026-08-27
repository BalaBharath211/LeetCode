class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        h=[0]*(n+1)
        for i in nums:
            if h[i]==0:
                h[i]=+1
            elif h[i]==1:
                return i

        