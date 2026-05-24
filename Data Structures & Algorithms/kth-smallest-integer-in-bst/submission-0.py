# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []
        def element(self,root,array):
            if root is None:
                return 
            else:
                array.append(root.val)
                element(self,root.left, array)
                element(self,root.right,array)
        
        element(self,root,array)

        array.sort()

        return array[k-1]