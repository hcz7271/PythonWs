from dllist import DoubleLinkedList


class Dictionary(object):
    """
    python字典的数据结构，用双链表来实现
    {bucket0,bucket1,bucket2,...,bucket256}
    每个bucket也是一个双链表 [key<->value0<->value1<->value2<->...]
    every bucket is a dllist
    """

    def __init__(self, num_buckets=256):
        """Initializes a Map with the given number of buckets."""
        self.map = DoubleLinkedList()
        for i in range(num_buckets):
            self.map.push(DoubleLinkedList())

    def hash_key(self, key):
        """Given a key this will create a # and then convert it to an index for the
        aMap's buckets.
        给一个键，返回这个键对应的bucket的索引值在map里边"""
        return hash(key) % self.map.count()

    def get_bucket(self, key):
        """输入一个键，返回一个包含键值对的节点bucket"""
        bucket_id = self.hash_key(key)
        return self.map.get(bucket_id)

    def get_slot(self, key, default=None):
        """
        Returns either the bucket and node for a slot, or None, None
        插槽
        """
        # an instance of bucket implemented by dllist
        bucket = self.get_bucket(key)

        if bucket:
            node = bucket.begin
            i = 0

            while node:
                if key == node.value[0]:
                    return bucket, node
                else:
                    node = node.next
                    i += 1

        return bucket, None

    def get(self, key, default=None):
        """Gets the value in a bucket for the given key, or the default."""
        bucket, node = self.get_slot(key, default=default)
        return node and node.value[1] or node

    def set(self, key, value):
        """
        字典dict的set方法实现
        Sets the key to the value, replacing any existing value."""
        bucket, slot = self.get_slot(key)

        if slot:
            # the key exists, replace it
            slot.value = (key, value)
        else:
            # the key does not, append to create it
            bucket.push((key, value))

    def delete(self, key):
        """Deletes the given key from the Map."""
        bucket = self.get_bucket(key)
        node = bucket.begin

        while node:
            k, v = node.value
            if key == k:
                bucket.detach_node(node)
                break

    def list(self):
        """Prints out what's in the Map."""
        bucket_node = self.map.begin
        while bucket_node:
            slot_node = bucket_node.value.begin
            while slot_node:
                print(slot_node.value)
                slot_node = slot_node.next
            bucket_node = bucket_node.next
