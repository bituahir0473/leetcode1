class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        a=0
        nums.sort()
        n=len(nums)
        for  i in range(0,n,2):
           
                a+=nums[i]
        return a