def bubble_sort(numbers: object):
    """Sorts a list of numbers using bubble sort."""
    while True:
        # start off assuming it's sorted
        is_sorted = True
        # comparing 2 at a time, skipping ahead
        node = numbers._header._next
        while node._next._value != None:
            # loop through comparing node to the next
            if node._value > node._next._value:
                # if the next is greater, then we need to swap
                node._value, node._next._value = node._next._value, node._value
                # oops, looks like we have to scan again
                is_sorted = False
            node = node._next

        # this is reset at the top but if we never swapped, it'ssorted
        if is_sorted:
            break
