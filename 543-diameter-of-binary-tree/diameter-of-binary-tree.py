# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # idea: time and space O(n)
        # we gonna check each node's left most node to right most node and find longest path
        # so, we need to calculate diameter and height for each node
            # diameter = left height + right height + 2
            # leaf node's height = 0
        
        # code:
        max_diameter = [0] # max() can only be used on iterable
        
        def dfs(root):
            # recursion base case, null's height is -1
            if not root: 
                return -1

            # calculate diameter
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            diameter = left_height + right_height + 2

            # update max_diameter
            max_diameter[0] = max(max_diameter[0], diameter)

            # calculate height
            return 1 + max(left_height, right_height)

        dfs(root)
        return max_diameter[0]