class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        p=[]
        count=0
        if set(nums)=={1}:
            return len(nums)
        if set(nums)=={0}:
            return 0
        for i in range(0, len(nums)):
            if nums[i]==1:
                count+=1
                p.append(count)
            else:
                count=0
        return max(p)
