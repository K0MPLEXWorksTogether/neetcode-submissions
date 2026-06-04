# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderHelper(self, root: Optional[TreeNode], accumulator: list[int]) -> None:
        if not root:
            return

        self.inorderHelper(root.left, accumulator)
        accumulator.append(root.val)
        self.inorderHelper(root.right, accumulator)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        self.inorderHelper(root, results)
        return results