def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inOrder(node):
            if not node: return
            inOrder(node.left)
            if len(res) == k:
               return 
            res.append(node.val)
            inOrder(node.right)

        inOrder(root)
        print(res)
        return res[-1]