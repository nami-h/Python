class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(0, k):
            x=nums.pop()
            nums.insert(0, x)
            
        
