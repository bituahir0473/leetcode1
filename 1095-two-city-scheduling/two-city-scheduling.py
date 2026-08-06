class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        n=len(costs)
        x=0
        for i in range(n):
            if i<n//2:
                x+=costs[i][0]
            else:
                x+=costs[i][1]
        return x