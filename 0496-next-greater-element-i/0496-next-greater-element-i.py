class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        res={}
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if not stack:
                res[nums2[i]]=-1
            else:
                res[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        result = []

        for num in nums1:
            result.append(res[num])
        return result
            

        