# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_d = [0]

        def height (root):
            if root is None:
                return 0
        
            l_height = height(root.left)
            r_height = height(root.right)
            d = l_height + r_height
            largest_d[0] = max(largest_d[0], d)
            return 1 + max(l_height, r_height)
        height(root)
        return largest_d[0]

