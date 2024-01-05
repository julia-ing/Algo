class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        def search(root):
            nonlocal res
            if not root:
                return 0
            leftSum = search(root.left)
            rightSum = search(root.right)
            res = max(res, leftSum + rightSum + root.val)
            return max(0, max(leftSum, rightSum) + root.val)

        res = float('-inf')
        search(root)
        return res
