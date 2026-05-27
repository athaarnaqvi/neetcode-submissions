# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if root is None:
                return 0
            
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)

            down = leftmax + rightmax + root.val
            either = max(leftmax,rightmax) + root.val
            neither = root.val

            self.res = max(self.res,down,either,neither)

            return max(either,neither)

        dfs(root)
        return self.res 