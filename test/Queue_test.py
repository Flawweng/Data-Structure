import unittest
from Queue import Queue

class QueueTest(unittest.TestCase):

    def test_equals(self):
        s = Queue(1,2,3,"Hello","World")
        t = Queue(1,2,3,"Hello","World")
        self.assertTrue(s.equals(Queue(1,2,3,"Hello","World"))) 
        self.assertFalse(s.equals(Queue(1,2,3,"Hello","World1"))) 
        self.assertFalse(s.equals(Queue(1,2,3,"Hello"))) 
    
    def test_enqueue(self):
        s = Queue()
        s.enqueue(1).enqueue("Hello")
        self.assertTrue(s.equals(Queue(1,"Hello")))

    def test_dequeue(self):
        s = Queue(1,2,3,"Hello","World")
        self.assertEqual(s.dequeue(),1)

    def test_front(self):
        s = Queue(1,2,3,"Hello","World")
        self.assertEqual(s.front(), 1)

    def test_rear(self):
        s = Queue(1,2,3,"Hello","World")
        self.assertEqual(s.rear(), "World")
    
    def test_size(self):
        s = Queue(1,2,3,"Hello","World")
        self.assertEqual(s.size(), 5)

    def test_empty(self):
        s = Queue()
        self.assertTrue(s.empty())
        s = Queue(1,2,3,"Hello","World")
        self.assertFalse(s.empty())

    def test_reverse(self):
        s = Queue(1,2,3,"Hello","World")
        s.reverse()
        self.assertTrue(s.equals(Queue("World","Hello",3,2,1)))
    
    def test_sort(self):
        s = Queue(-3,15,18,-5,30)
        s.sort()
        print( " final value " + str(s))
        self.assertTrue(s.equals(Queue(-5,-3,15,18,30)))

if __name__ == '__main__':
    unittest.main()
