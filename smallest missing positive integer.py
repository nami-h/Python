class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        min_val=1
        for i in nums:
            if min_val==i:
                min_val+=1
        return min_val
    
            
