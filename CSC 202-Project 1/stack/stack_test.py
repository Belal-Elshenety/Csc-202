import unittest
import stack_array
import stack_linked_list

class MyTestCase(unittest.TestCase):
    def test_is_empty_array(self):
        stack1 = stack_array.StackArray(5)
        stack1.push(1)
        self.assertFalse(stack1.is_empty())

    def test_is_empty_linked_list(self):
        stack2 = stack_linked_list.StackLinkedList(5)
        stack2.push(1)
        self.assertFalse(stack2.is_empty())

    def test_is_full_array(self):
        stack1 = stack_array.StackArray(5)
        for n in range(4):
            stack1.push(n)
        self.assertFalse(stack1.is_full())

    def test_is_full_linked_list(self):
        stack2 = stack_linked_list.StackLinkedList(5)
        for n in range(4):
            stack2.push(n)
        self.assertFalse(stack2.is_full())

    def test_peek_array(self):
        stack1 = stack_array.StackArray(5)
        for num in range(1, 5):
            stack1.push(num)
        self.assertEqual(stack1.peek(), 4)

    def test_peek_linked_list(self):
        stack2 = stack_linked_list.StackLinkedList(5)
        for num in range(1, 5):
            stack2.push(num)
        self.assertEqual(stack2.peek(), 4)


    def test_push_pop_peek_array(self):
        stack1 = stack_array.StackArray(5)
        for n in range(1,4):
            stack1.push(n)
        self.assertEqual(stack1.pop(), 3)
        self.assertEqual(stack1.peek(), 2)
        self.assertEqual(stack1.pop(), 2)

    def test_push_pop_peek_linked_list(self):
        stack2 = stack_linked_list.StackLinkedList(5)
        for n in range(1,4):
            stack2.push(n)
        self.assertEqual(stack2.pop(), 3)
        self.assertEqual(stack2.peek(), 2)
        self.assertEqual(stack2.pop(), 2)

    def test_size_array(self):
        stack1 = stack_array.StackArray(5)
        self.assertEqual(stack1.num_items, 0)
        stack1.push(1)
        stack1.push(2)
        self.assertEqual(stack1.num_items, 2)
        stack1.pop()
        stack1.pop()
        self.assertEqual(stack1.num_items, 0)

    def test_size_linked_list(self):
        stack2 = stack_linked_list.StackLinkedList(5)
        self.assertEqual(stack2.num_items, 0)
        stack2.push(1)
        stack2.push(2)
        self.assertEqual(stack2.num_items, 2)
        stack2.pop()
        stack2.pop()
        self.assertEqual(stack2.num_items, 0)



if __name__ == '__main__':
    unittest.main()
