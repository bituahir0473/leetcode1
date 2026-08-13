class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        c=0
        for i in str(n):
            if i==str(x):
                c+=1
        if c>=1 and str(n)[0]!=str(x):
            return True
        else:
            return False

