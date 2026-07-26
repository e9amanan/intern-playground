from collections import deque
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    """
    A Queue implementation  (FIFO)

    """

    def __init__(self) -> None:
        self._items: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        """Adds an item to the back of the queue. Time: O(1)."""
        self._items.append(item)

    def dequeue(self) -> T:
        """Removes and returns the front item. Time: O(1). Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self) -> Optional[T]:
        """Returns the front item without removing it. Time: O(1)."""
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        """Returns True if the queue is empty. Time: O(1)."""
        return len(self._items) == 0

    def size(self) -> int:
        """Returns the number of elements in the queue. Time: O(1)."""
        return len(self._items)
