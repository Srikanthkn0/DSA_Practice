# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float("inf")
        def dfs(root):
            nonlocal res
            if not root:
                return None
            left = self.getmax(root.left)
            right = self.getmax(root.right)
            res = max(res, root.val + left + right)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return res
    
    def getmax(self,root):
        if not root:
            return 0
        left = self.getmax(root.left)
        right = self.getmax(root.right)
        
        return max(0,root.val + max(left,right))