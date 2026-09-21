import copy

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        res = []

        candidates.sort()


        def dfs(i,curr_res, curr_sum):


            if curr_sum == target:
                res.append(copy.deepcopy(curr_res))
                return

            if i>len(candidates)-1 or curr_sum>target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if curr_sum + candidates[j] > target:
                    break
                curr_res.append(candidates[j])
                dfs(j + 1, curr_res, curr_sum + candidates[j])
                curr_res.pop()


        
        dfs(0,[], 0)

        return res