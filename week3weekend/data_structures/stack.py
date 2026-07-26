from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """
    A Stack implementation using a Python list (LIFO)
    """

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Adds an item to the top of the stack. Time: O(1) amortized."""
        self._items.append(item)

    def pop(self) -> T:
        """Removes and returns the top item. Time: O(1). Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Optional[T]:
        """Returns the top item without removing it. Time: O(1)."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        """Returns True if the stack is empty. Time: O(1)."""
        return len(self._items) == 0

    def size(self) -> int:
        """Returns the number of elements in the stack. Time: O(1)."""
        return len(self._items)
