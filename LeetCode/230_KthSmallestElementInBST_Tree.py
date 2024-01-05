class Solution:
    def kthSmallest(self, root, k):
        def inorder(root):
            if root:
                return inorder(root.left) + [root.val] + inorder(root.right)
            else:
                return []

        res = inorder(root)
        return res[k-1]
