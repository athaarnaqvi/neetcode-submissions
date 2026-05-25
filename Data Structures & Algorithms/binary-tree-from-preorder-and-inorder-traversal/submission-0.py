# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for idx, val in enumerate(inorder):
            hashmap[val] = idx
    
        self.index = 0 
        def dfs(l,r):
            if l > r:
                return None
            
            rootval = preorder[self.index]
            self.index += 1
            root = TreeNode(rootval)
            mid = hashmap[rootval]
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            print(root.val)

            return root
        
        return dfs(0,len(inorder)-1)


            
             
