import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right    

def rightSideView(root: TreeNode) -> list[int]:
        q = collections.deque()
        if root:
            q.append(root)
        res = []

        while q:
            rightMost = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightMost = node
                    q.append(node.left)
                    q.append(node.right)
            if rightMost:
                res.append(rightMost.val)
        return res