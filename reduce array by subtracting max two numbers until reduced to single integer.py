class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while(len(stones)!=1):
            m1=max(stones)
            stones.remove(m1)
            m2=max(stones)
            stones.remove(m2)
            sub=m1-m2
            if sub<0:
                sub*=-1
            stones.append(sub)
            
        integer=''.join(str(i) for i in stones)
            
        return int(integer)
        
