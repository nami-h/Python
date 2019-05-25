class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in range(1,len(A)+1):
            if i not in set(A):
                return i
            x = i
        return x+1
