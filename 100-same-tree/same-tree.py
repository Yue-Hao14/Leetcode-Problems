# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # idea: O(p+q)
        # check each node from top down to see if each node in p and q are the same

        # code:
        # if both of them null, then same tree
        if not p and not q:
            return True
        # if one of them null, the other not null, then not same tree
        if not p or not q:
            return False
        # if node's val not the same, then not same tree
        if p.val != q.val:
            return False
        
        # after checking curr node's val, now recursive step to check other nodes to see if they are the same as well
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))