from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):

    def __init__(self) -> None:
        self._items: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def deque(self) -> t:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0


def test_queue() -> None:
    q = Queue[str]()
    assert q.is_empty() == True
    q.enqueue("task1")
    q.enqueue("task2")
    assert q.peek() == "task1"
    assert q.dequeue() == "task1"
    assert q.dequeue() == "task2"
    assert q.is_empty() == True


test_queue()
