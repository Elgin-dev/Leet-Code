class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtrack(index,curr):
            res.append(curr[:])
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                else:
                    curr.append(nums[i])    
                backtrack(i+1,curr)
                curr.pop()
        backtrack(0,[])
        return res        