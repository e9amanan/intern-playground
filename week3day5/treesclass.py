from typing import List, Optional


class TreeNode:
    """definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """first left then right"""
    result = []

    def traverse(node):
        """traversal through tree"""
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)

    traverse(root)
    return result
