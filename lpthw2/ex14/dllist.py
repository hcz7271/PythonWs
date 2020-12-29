class _DoubleLinkedList:
    class _Node:
        __slots__ = "_value", "_prev", "_next"

        def __init__(self, _value, _prev, _next):
            self._value = _value
            self._prev = _prev
            self._next = _next

        def __repr__(self):
            pval = self._prev and self._prev._value or None
            nval = self._next and self._next._value or None
            return f"[{self._value}, {repr(pval)}, {repr(nval)}]"

    def __init__(self):
        self._begin = None
        self._end = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _invariant(self):
        if self.is_empty():
            assert (self._begin == None) and (self._end == None)
        else:
            if self.__len__() == 1:
                assert self._begin == self._end
            assert (self._begin._prev == None) and (self._end._next == None)

    def push(self, obj):
        if self._end:
            node = self._Node(obj, self._end, None)
            self._end._next = node
            self._end = node
        else:
            self._begin = self._Node(obj, None, None)
            self._end = self._begin

    def pop(self):
        if self._end:
            # get the last node
            node = self._end

            if self._end == self._begin:
                # last node, kill them both
                self._end = None
                self._begin = None
            else:
                # not last, detach and move _end
                self._end = node._prev
                self._end._next = None

                if self._end == self._begin:
                    # we have only one node left, make _begin and _end same
                    self._begin._next = None

            return node._value
        else:
            return None

    def unshift(self):
        if self._begin:
            node = self._begin

            if self._end == self._begin:
                self._end = None
                self._begin = None
            else:
                self._begin = node._next
                self._begin._prev = None

            return node._value
        else:
            return None

    def shift(self, obj):
        self.push(obj)

    def detach_node(self, node):
        if node == self._end:
            # only node or last node
            self.pop()
        elif node == self._begin:
            # first node
            self.unshift()
        else:
            # in the middle
            _prev = node._prev
            nxt = node._next
            _prev._next = nxt
            nxt._prev = _prev

    def remove(self, obj):
        node = self._begin
        count = 0

        while node:
            if node._value == obj:
                self.detach_node(node)
                return count
            else:
                count += 1
                node = node._next

        return -1

    def first(self):
        return self._begin and self._begin._value or None

    def last(self):
        return self._end and self._end._value or None

    def get(self, index):
        node = self._begin
        i = 0
        while node:
            if i == index:
                return node._value
            else:
                i += 1
                node = node._next

        return None

    def dump(self, mark="----"):
        node = self._begin
        print(mark)
        while node:
            print(node, " ", _end="")
            node = node._next
        print()
