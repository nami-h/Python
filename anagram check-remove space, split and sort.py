class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.replace(' ', '')
        t.replace(' ', '')
        s=s.split()
        t=t.split()
        if s.sort()==t.sort():
            return True
