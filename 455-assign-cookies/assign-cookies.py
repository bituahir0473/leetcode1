class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c=0
        g.sort()
        s.sort()
        for i in s:
            if i>=g[c]:
                c+=1
            if c==len(g):
               break
        return c