class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        wlh=[]
        wfh=[]    
        for i in range(n-1):
          wlh.append(nums[i+1])
          wfh.append(nums[i]) 
        a=self.helper(wlh)
        b=self.helper(wfh) 
        return max(a,b)  

    def helper(self,nums):
        
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])

        for i in range(2,n):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])      
        return dp[n-1]      
