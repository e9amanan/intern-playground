from typing import Any, List, Optional


class TreeNode:
    def __init__(self, val: Any):
        self.val = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class BST:
    """
    Binary Search Tree implementation.
    """

    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, val: Any) -> None:
        if not self.root:
            self.root = TreeNode(val)
            return
        self._insert_recursive(self.root, val)

    def _insert_recursive(self, node: TreeNode, val: Any) -> None:
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)

    def search(self, val: Any) -> bool:
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node: Optional[TreeNode], val: Any) -> bool:
        if node is None:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)

    def delete(self, val: Any) -> None:
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(
        self, node: Optional[TreeNode], val: Any
    ) -> Optional[TreeNode]:
        if node is None:
            return node

        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_larger_node = self._find_min(node.right)
            node.val = min_larger_node.val
            node.right = self._delete_recursive(node.right, min_larger_node.val)

        return node

    def _find_min(self, node: TreeNode) -> TreeNode:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self) -> List[Any]:
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[TreeNode], result: List[Any]):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)

    def preorder(self) -> List[Any]:
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: Optional[TreeNode], result: List[Any]):
        if node:
            result.append(node.val)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self) -> List[Any]:
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: Optional[TreeNode], result: List[Any]):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.val)
