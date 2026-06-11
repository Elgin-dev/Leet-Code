#top down approach 
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
            n=len(cost)
            memo={0:0,1:0}
            def min_cos(i):
                if i in memo:
                    return memo[i]
                else:
                    memo[i]=min(cost[i-2]+min_cos(i-2),cost[i-1]+min_cos(i-1))
                    return memo[i]
                  
            return min_cos(n)      




#bottom up approach

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0] *(n+1)
        for i in range(2,n+1):
            dp[i]=min((dp[i-2]+cost[i-2]),(dp[i-1]+cost[i-1]))
        return dp[n]    