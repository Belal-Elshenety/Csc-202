import unittest
import queue_array
import queue_linked_list

class MyTestCase(unittest.TestCase):
    def test_queue_is_empty_array(self):
        queue1 = queue_array.QueueArray(5)
        queue1.enqueue(1)
        self.assertFalse(queue1.is_empty())

    def test_queue_is_empty_linked_list(self):
        queue2 = queue_linked_list.QueuekLinkedList(5)
        queue2.enqueue(1)
        self.assertFalse(queue2.is_empty())

    def test_queue_is_full_array(self):
        queue1 = queue_array.QueueArray(5)
        for n in range(4):
            queue1.enqueue(n)
        self.assertFalse(queue1.is_full())

    def test_queue_is_full_linked_list(self):
        queue2 = queue_linked_list.QueuekLinkedList(5)
        for n in range(4):
            queue2.enqueue(n)
        self.assertFalse(queue2.is_full())

    def test_queue_enqueue_dequeue_array(self):
        queue1 = queue_array.QueueArray(5)
        for n in range(4):
            queue1.enqueue(n)
        self.assertEqual(queue1.num_items, 4)
        self.assertEqual(queue1.dequeue(), 0)
        self.assertEqual(queue1.dequeue(), 1)

    def test_queue_enqueue_dequeue_linked_list(self):

        queue2 = queue_linked_list.QueuekLinkedList(5)
        for n in range(4):
            queue2.enqueue(n)
        self.assertEqual(queue2.num_items, 4)
        self.assertEqual(queue2.dequeue(), 0)
        self.assertEqual(queue2.dequeue(), 1)


    def test_peek_array(self):
        queue1 = queue_array.QueueArray(5)
        for n in range(4):
            queue1.enqueue(n)
        self.assertEqual(queue1.peek(), 0)
        queue1.dequeue()
        queue1.dequeue()
        self.assertEqual(queue1.peek(), 2)

    def test_peek_linked_list(self):
        queue2 = queue_linked_list.QueuekLinkedList(5)
        for n in range(4):
            queue2.enqueue(n)
        self.assertEqual(queue2.peek(), 0)
        queue2.dequeue()
        queue2.dequeue()
        self.assertEqual(queue2.peek(), 2)

    def test_queue_size_array(self):
        queue1 = queue_array.QueueArray(5)
        for n in range(4):
            queue1.enqueue(n)
        self.assertEqual(queue1.size(), 4)
        queue1.dequeue()
        queue1.dequeue()
        self.assertEqual(queue1.size(), 2)

    def test_queue_size_linked_list(self):
        queue2 = queue_linked_list.QueuekLinkedList(5)
        for n in range(4):
            queue2.enqueue(n)
        self.assertEqual(queue2.size(), 4)
        queue2.dequeue()
        queue2.dequeue()
        self.assertEqual(queue2.size(), 2)





if __name__ == '__main__':
    unittest.main()
