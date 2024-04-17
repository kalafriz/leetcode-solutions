# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        self.result = ""
        
        def dfs(node, s):
            
            if not node:
                #print("Dead end!")
                return "zz" # greater than z
            
            s = chr(node.val+97) + s
            
            if not node.left and not node.right: # is leaf
                #print("leaf: ", chr(node.val+97))
                if self.result > s or self.result=="":
                    self.result = s
            
            if node.left:
                dfs(node.left, s)
            if node.right:
                dfs(node.right, s)
        
        dfs(root, "")
        return self.result