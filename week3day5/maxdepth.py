"""import math
from collections import deque"""

from typing import Optional


class TreeNode:
    """definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxheight(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    leftheight = maxheight(root.left)
    rightheight = maxheight(root.right)

    return 1 + max(leftheight, rightheight)
