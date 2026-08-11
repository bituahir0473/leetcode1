class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        comb=[]
        def backtrack(start):
            if len(comb)==k:
                res.append(comb[::])
                return 
            for x in range(start,n+1):
                comb.append(x)
                backtrack(x+1)
                comb.pop()
        backtrack(1)
        return res