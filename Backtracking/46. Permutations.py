from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr):
            # Base case: permutation is complete
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for num in nums:
                # Avoid using the same number twice
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        backtrack([])
        return res