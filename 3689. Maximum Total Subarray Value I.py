class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxi=max(nums)
        mini=min(nums)
        a=maxi-mini
        ans=0
        for i in range(k):
            ans=ans+a
        return ans    




        