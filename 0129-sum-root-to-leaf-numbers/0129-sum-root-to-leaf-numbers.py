# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, path):
            
            if not node:
                return 0
            
            path = int(str(path)+str(node.val)) # concat paths as strings -> int
            
            if not node.left and not node.right:
                return path
            
            return dfs(node.left, path) + dfs(node.right, path)
        
        return dfs(root, 0)