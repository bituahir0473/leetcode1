class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        mx=float('-inf')
        
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    mx=max(mx,(nums[i]-nums[j])*nums[k])
        return mx if mx >0 else 0
