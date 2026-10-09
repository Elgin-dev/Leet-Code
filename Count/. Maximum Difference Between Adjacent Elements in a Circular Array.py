1.Given a circular array nums, find the maximum absolute difference between adjacent elements. In a circular array, the first and last elements are also considered adjacent.

Example 1:
Input: nums = [1,2,4]
Output: 3
Explanation:
Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

Example 2:
Input: nums = [-5,-10,-5]
Output: 5
Explanation:
The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.

2.Approach:
  *Iterate through the array and calculate the absolute difference between adjacent elements.
  *Include the circular connection, where the last element is adjacent to the first element.
  *Find the maximum absolute difference among all computed values.

3.solution.py:
class Solution(object):
    def maxAdjacentDistance(self, nums):
        max_diff = 0  # Variable to track max absolute difference
        
        for i in range(len(nums)):
            if i == len(nums) - 1:  # Last element connects to the first
                diff = abs(nums[-1] - nums[0])
            else:
                diff = abs(nums[i] - nums[i+1])  # Regular adjacency
            
            max_diff = max(max_diff, diff)  # Update max difference
        
        return max_diff



4.Time Complexity: O(N)
