
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def bfs(root, val, depth, curr):

            if curr == depth - 1:
                right = root.right
                left = root.left

                root.right = TreeNode(val, right=right)
                root.left = TreeNode(val, left=left)
            else:
                if root.right:
                    bfs(root.right, val, depth, curr + 1)
                if root.left:
                    bfs(root.left, val, depth, curr + 1)
        
        if depth == 1:
            return TreeNode(val, left=root)
        else:
            bfs(root, val, depth, 1)
            return root