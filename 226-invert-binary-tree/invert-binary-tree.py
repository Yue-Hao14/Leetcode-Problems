# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recrusive base case
        if not root: return None

        # swap left and right
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # do recursion
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root