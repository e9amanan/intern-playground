from typing import Generic, List, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._item.pop()

    def peek(self) -> t:
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)


def test_stack() -> None:
    s = Stack[int]()
    assert s.is_empty() == True
    s.push(10)
    s.push(20)
    assert s.peek() == 20
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.is_empty == True

    try:
        s.pop()
        assert False, "should have raised IndexError "
    except IndexError:
        pass


test_stack()
