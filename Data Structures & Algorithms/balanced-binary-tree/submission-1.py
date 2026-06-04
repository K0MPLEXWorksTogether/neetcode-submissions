# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxHeight(self, root):
        if not root:
            return 0

        return 1 + max(
            self.maxHeight(root.left),
            self.maxHeight(root.right)
        )

    def isBalanced(self, root):
        if not root:
            return True

        left_height = self.maxHeight(root.left)
        right_height = self.maxHeight(root.right)

        return (
            abs(left_height - right_height) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )