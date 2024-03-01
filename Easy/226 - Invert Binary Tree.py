def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def invert(root):
        if not root:
            return 
        
        root.right, root.left = root.left, root.right
        
        invert(root.right)
        invert(root.left)
    
    invert(root)
    return root