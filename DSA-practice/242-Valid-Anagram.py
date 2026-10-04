#1st solution i could think of-make two new list add characte sort them and compare

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        L=[]
        S=[]
        for i in s:
            L.append(i)
        for i in t:
            S.append(i)
        a=sorted(L)
        b=sorted(S)
        if a==b:
            return True
        else:
            return False
        