import pytest
from data_structures.bst import BST


def test_bst_insert_and_search():
    bst = BST()
    assert bst.search(10) is False  # Empty tree

    bst.insert(10)
    bst.insert(5)
    bst.insert(15)

    assert bst.search(10) is True
    assert bst.search(5) is True
    assert bst.search(20) is False


def test_bst_traversals():
    bst = BST()
    elements = [10, 5, 15, 3, 7, 18]
    for el in elements:
        bst.insert(el)

    assert bst.inorder() == [3, 5, 7, 10, 15, 18]
    assert bst.preorder() == [10, 5, 3, 7, 15, 18]
    assert bst.postorder() == [3, 7, 5, 18, 15, 10]


def test_bst_delete():
    bst = BST()
    elements = [10, 5, 15, 3, 7, 12, 18]
    for el in elements:
        bst.insert(el)

    # Delete leaf
    bst.delete(3)
    assert bst.inorder() == [5, 7, 10, 12, 15, 18]

    # Delete node with one child (let's manipulate to create one)
    bst.delete(7)
    assert bst.inorder() == [5, 10, 12, 15, 18]

    # Delete node with two children
    bst.delete(15)
    assert bst.inorder() == [5, 10, 12, 18]
