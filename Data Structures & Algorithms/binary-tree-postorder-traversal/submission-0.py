# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], accumulator: list[int]) -> None:
        if not root:
            return

        
        self.helper(root.left, accumulator)
        self.helper(root.right, accumulator)
        accumulator.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        self.helper(root, results)
        return results