# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            top = TreeNode(val, left=root)
            return top
        
        if root:
            if depth == 2:
                l = TreeNode(val, left=root.left)
                r = TreeNode(val, right=root.right)
                root.left = l
                root.right = r

            else:
                root.left = self.addOneRow(root.left, val, depth-1)
                root.right = self.addOneRow(root.right, val, depth-1)
            
        return root
        
        
        