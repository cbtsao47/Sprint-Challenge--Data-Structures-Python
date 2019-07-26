#
# A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.
# rules
# 1. when full, oldest element is overwritten with ther newest
# 2. initialize the storage with an array of None
# 3. don't return None values
# Implement this behavior in the RingBuffer class. RingBuffer has two methods, append and get. The append method adds elements to the buffer. The get method returns all of the elements in the buffer in a list in their given order. It should not return any None values in the list even if they are present in the ring buffer.


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.current >= self.capacity:
            self.current = 0
        self.storage[self.current] = item
        self.current += 1

    def get(self):
        return [element for element in self.storage if element != None]
