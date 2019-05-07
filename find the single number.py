class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        x=sum(set(nums))
        y=sum(nums)
        return 2*x-y
