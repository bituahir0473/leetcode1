class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sol=[]
        n=len(nums)
        def backtrack(i):
            if (i==n):
                res.append(sol[:])
                return
            backtrack(i+1)          # not choose 
            sol.append(nums[i])
            backtrack(i+1)          # when we choose
            sol.pop()
        backtrack(0)
        return res
