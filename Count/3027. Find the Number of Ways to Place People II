You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

We define the right direction as positive x-axis (increasing x-coordinate) and the left direction as negative x-axis (decreasing x-coordinate). Similarly, we define the up direction as positive y-axis (increasing y-coordinate) and the down direction as negative y-axis (decreasing y-coordinate)

You have to place n people, including Alice and Bob, at these points such that there is exactly one person at every point. Alice wants to be alone with Bob, so Alice will build a rectangular fence with Alice's position as the upper left corner and Bob's position as the lower right corner of the fence (Note that the fence might not enclose any area, i.e. it can be a line). If any person other than Alice and Bob is either inside the fence or on the fence, Alice will be sad.

Return the number of pairs of points where you can place Alice and Bob, such that Alice does not become sad on building the fence.

Note that Alice can only build a fence with Alice's position as the upper left corner, and Bob's position as the lower right corner. For example, Alice cannot build either of the fences in the picture below with four corners (1, 1), (1, 3), (3, 1), and (3, 3), because:

With Alice at (3, 3) and Bob at (1, 1), Alice's position is not the upper left corner and Bob's position is not the lower right corner of the fence.
With Alice at (1, 3) and Bob at (1, 1), Bob's position is not the lower right corner of the fence.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 0
Explanation: There is no way to place Alice and Bob such that Alice can build a fence with Alice's position as the upper left corner and Bob's position as the lower right corner. Hence we return 0. 

Algorithm:
*Sort the Points Sort all points by increasing x-coordinate. If x is equal, sort by decreasing y-coordinate to prioritize higher points first.
*Initialize Counters Set pair = 0 to count valid pairs. Loop through each point i as the potential starting point.
*Set Y-Boundaries For each point i, define uppery = points[i][1] and initialize lowery = -∞ to track the lowest y-value already paired.
*Find Valid Pair Candidates Loop through points j > i. If points[j][1] ≤ uppery and > lowery, count it as a valid pair, update lowery, and continue.
*Early Termination If points[j][1] == uppery, break early—no better match can exist for this i.


Solution.py:
class Solution(object):
    def numberOfPairs(self, points):
        points.sort(key=lambda x :(x[0],-x[1]))
        pair=0
        n=len(points)
        for i in range(n):
            uppery=points[i][1]
            lowery=float('-inf')
            for j in range(i+1,n):
                currenty=points[j][1]
                if currenty<=uppery and currenty>lowery:
                    pair+=1
                    lowery=currenty
                    if currenty==uppery:
                        break
        return pair                 

Time complexity: O(n^2)
