"""import math
from collections import deque"""

from typing import Optional


class TreeNode:
    """definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inverttree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    root.left, root.right = root.right, root.left

    inverttree(root.left)
    inverttree(root.right)

    return root
