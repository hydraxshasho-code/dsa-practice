<<<<<<< HEAD
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        x,y=0,len(s)-1
        while x<y:
            s[x],s[y]=s[y],s[x]
            x+=1
            y-=1
=======
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        x,y=0,len(s)-1
        while x<y:
            s[x],s[y]=s[y],s[x]
            x+=1
            y-=1
>>>>>>> bd7feed (fixed the 0byte-206-reverse-linked)
