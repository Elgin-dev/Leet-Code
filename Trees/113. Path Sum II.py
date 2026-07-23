# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(node,path,tot):
            if not node:
                return 
            path.append(node.val)
            tot+=node.val
            if not node.left and not node.right and tot==targetSum:
                res.append(list(path))
            dfs(node.left,path,tot)
            dfs(node.right,path,tot)
            path.pop()
        dfs(root,[],0)
        return res        
                    