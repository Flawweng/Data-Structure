import unittest
from Stack import Stack

class StackTest(unittest.TestCase):

    def test_equals(self):
        s = Stack(1,2,3,"Hello","World")
        t = Stack(1,2,3,"Hello","World")
        self.assertTrue(s.equals(Stack(1,2,3,"Hello","World"))) 
        self.assertFalse(s.equals(Stack(1,2,3,"Hello","World1"))) 
        self.assertFalse(s.equals(Stack(1,2,3,"Hello"))) 
    
    def test_push(self):
        s = Stack()
        s.push(1).push("Hello")
        self.assertTrue(s.equals(Stack(1,"Hello")))

    def test_top(self):
        s = Stack(1,2,3,"Hello","World")
        self.assertEqual(s.top(), "World")

    def test_peek(self):
        s = Stack(1,2,3,"Hello","World")
        self.assertEqual(s.peek(), 1)
    
    def test_size(self):
        s = Stack(1,2,3,"Hello","World")
        self.assertEqual(s.size(), 5)

    def test_empty(self):
        s = Stack()
        self.assertTrue(s.empty())
        s = Stack(1,2,3,"Hello","World")
        self.assertFalse(s.empty())

if __name__ == '__main__':
    unittest.main()
