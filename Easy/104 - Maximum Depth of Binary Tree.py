def maxDepth(root) -> int:
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.right), maxDepth(root.left))