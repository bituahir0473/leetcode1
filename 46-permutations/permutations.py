class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        prem=permutations(nums)
        return(list(prem))