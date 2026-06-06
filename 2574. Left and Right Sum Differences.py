class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        thresh = len(nums)

        left_sum = []
        right_sum = []
        ans = []

        ls = 0
        rs = 0

        left_sum.append(0)
        for i in range(thresh - 1):
            ls += nums[i]
            left_sum.append(ls)
        right_sum = [0] * thresh
        for i in range(thresh - 2, -1, -1):
            rs += nums[i + 1]
            right_sum[i] = rs
        for i in range(len(nums)):
            a = abs(left_sum[i] - right_sum[i])
            ans.append(a)

        return ans