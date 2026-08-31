class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        prefixSum=0
        prefix_counts={}
        prefix_counts[0]=1
        for i in range(n):
            prefixSum+=nums[i]
            remove=prefixSum-k
            if remove in prefix_counts:
                count+=prefix_counts[remove]
            prefix_counts[prefixSum]=prefix_counts.get(prefixSum,0)+1
        return count

        