# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.serial = ""

        def dfs(root):
            if root is None:
                self.serial += "N,"
                
                return
            
            self.serial+=str(root.val)
            self.serial+=","
            dfs(root.left)
            dfs(root.right)
           

        dfs(root)   
        print(self.serial) 
        return self.serial

                    
     
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.root = None
        data = data.split(",")
        self.i = 0 
        def construct():
            if data[self.i] == "N" or self.i>len(data):
                self.i+=1
                return None
            
            current = TreeNode(data[self.i])
            if self.i == 0:
                self.root = current
            self.i+=1
            current.left = construct()
            current.right = construct()

            return current
        construct()
        return self.root



