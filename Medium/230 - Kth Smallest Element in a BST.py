def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inOrder(node):
            if not node: return
            inOrder(node.left)
            if len(res) == k:
               return 
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        print(res)
        return res[-1]