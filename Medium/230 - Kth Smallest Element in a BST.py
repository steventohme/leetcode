class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
        res = []

        def inOrder(node):
            if not node: return
            inOrder(node.left)
            if len(res) == k:
               return 
            res.append(node.val)
            inOrder(node.right)

        inOrder(root)
        return res[-1]