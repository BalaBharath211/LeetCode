class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        count=0
        least = float('-inf') 
        longest = 1
        for i in range(len(nums)):
                if nums[i]-1==least:
                    count+=1
                    least=nums[i]
                elif nums[i]!=least:
                    count=1
                    least=nums[i]
                longest=max(longest,count)
        return longest
                


        