# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # idea: O(n)
        # find left and right height of each node
        # if diff <= 1 and its own left and right node both balanced, then current node is balanced

        # code:
        def dfs(root):
            if not root: 
                return [True, 0]

            # calculate left and right nodes' height
            left = dfs(root.left)
            right = dfs(root.right)

            # when left and right node both balanced, and their height diff <= 1, then balanced
            balanced = (left[0] == True and right[0] == True and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        # call dfs function
        res = dfs(root)
    
        return res[0]


        