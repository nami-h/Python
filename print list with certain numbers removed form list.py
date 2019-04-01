class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for n in nums[0:]:
            if n==val:
                nums.remove(n)
        print(nums)
