class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            low = i + 1
            high = len(nums) - 1

            while low < high:

                total = nums[i] + nums[low] + nums[high]

                if total == 0:

                    ans.append([nums[i], nums[low], nums[high]])

                    low += 1
                    high -= 1

                    while low < high and nums[low] == nums[low - 1]:
                        low += 1

                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

                elif total < 0:
                    low += 1

                else:
                    high -= 1

        return ans