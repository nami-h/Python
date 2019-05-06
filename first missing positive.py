class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 1
        elif len(nums)==1:
            if nums==[1]:
                return 2
            else:
                return 1
        minimum=1
        nums.sort()
        while(max(nums)):
            if minimum in nums:
                minimum+=1
            else:
                return minimum
