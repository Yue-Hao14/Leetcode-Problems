# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # idea:
        # pre-order transversal both trees and push each node to an array
        # if 2 array ==, then same

        # code:
        p_arr = []
        q_arr = []

        def pre_order_dfs(root):
            if not root:
                return [None]

            return [root.val] + pre_order_dfs(root.left) + pre_order_dfs(root.right)
        
        p_arr = pre_order_dfs(p)
        q_arr = pre_order_dfs(q)

        return p_arr == q_arr