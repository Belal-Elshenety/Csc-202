class QueuekLinkedList:
    """Implements an efficient first-in first-out Abstract Data Type using a linked List"""

    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self, capacity):
        """Creates and empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.num_items = 0  # number of elements in the queue
        self.front = None
        self.back = None

    def is_empty(self):
        """Returns true if the queue self is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns true if the queue self is full and false otherwise"""
        return self.num_items == self.capacity

    def enqueue(self, item):
        """Adds item to the queue"""
        data = self.Node(item)
        if self.back is None:
            self.back = data
            self.front = data
        else:
            self.back.next = data
            self.back = self.back.next
        self.num_items += 1

    def dequeue(self):
        """Returns the current front of the queue"""
        item = self.front.item
        self.front = self.front.next
        self.num_items -= 1
        return item

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        return self.front.item

    def size(self):
        """Returns the number of elements currently in the queue, not the capacity"""
        return self.num_items
