"""
from collections import deque"""

import math
from typing import Optional


class TreeNode:
    """definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validbst(root: Optional[TreeNode]) -> bool:
    def validate(node, low=-math.inf, high=math.inf):
        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False

        return validate(node.left, low, node.val) and validate(
            node.right, node.val, high
        )

    return validate(root)
