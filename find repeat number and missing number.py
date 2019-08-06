class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        X=[]
        a=[]
        for i in A:
            a.append(i)
        sorted(a)
        L=sum(a)-sum(set(a))
        X.append(L)
        B=[int(i) for i in range(1, max(a))]
        for i in B:
            if i not in a:
                X.append(i)
        return X
