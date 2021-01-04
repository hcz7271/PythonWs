import pytest
import sorting
from dllist import DoubleLinkedDeque
from random import randint

max_numbers = 5


def random_list(count: int) -> object:
    numbers = DoubleLinkedDeque()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10000))
    return numbers


def is_sorted(numbers: object) -> bool:
    node = numbers._header._next
    while node._next._value != None:
        if node._value > node._next._value:
            return False
        else:
            node = node._next
    return True


def test_bubble_sort():
    numbers = random_list(max_numbers)
    sorting.bubble_sort(numbers)
    assert is_sorted(numbers)


if __name__ == "__main__":
    print("testing")
    n1 = random_list(max_numbers)
    n1.show_in_list()
    sorting.bubble_sort(n1)
    n1.show_in_list()
    pytest.main()