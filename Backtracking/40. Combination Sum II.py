class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(start,curr,remain):
            if remain==0:
                res.append(curr[:])
                return
            if remain<0:
                return

            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                
                curr.append(candidates[i])
                backtrack(i+1,curr,remain-candidates[i])
                curr.pop()    
        backtrack(0,[],target)
        return res        