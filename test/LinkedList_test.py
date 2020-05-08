import unittest
from LinkedList import LinkedList

class LinkedListTest(unittest.TestCase):

    def test_equals(self):
        l = LinkedList(1,2,3,'Hello','World') 
        m = LinkedList(1,2,3,'Hello','World')
        self.assertTrue(l.equals(m))

    def test_push(self):
        l = LinkedList(1,2,3,'Hello','World') 
        self.assertTrue(l.push(0).equals(LinkedList(0,1,2,3,'Hello','World')))

    def test_append(self):
        l = LinkedList(1,2,3,'Hello','World') 
        l.append('!')
        self.assertEqual(l.size, 6)
        self.assertTrue(l.equals(LinkedList(1,2,3,'Hello','World','!'))) 
    
    def test_addAtIndex(self):
        l = LinkedList(1,2,3,'Hello','World') 
        l.addAtIndex(4,3)
        self.assertEqual(l.size, 6)
        self.assertTrue(l.equals(LinkedList(1,2,3,4,'Hello','World')))

    def test_removeAtIndex(self):
        l = LinkedList(1,2,3,'Hello','World') 
        l.removeAtIndex(4)
        self.assertTrue(l.equals(LinkedList(1,2,3,'Hello')))

    def test_remove(self):
        l = LinkedList(1,2,3,'Hello','World') 
        self.assertTrue(l.remove(1).equals(LinkedList(2,3,'Hello','World')))
        l = LinkedList(1,2,3,'Hello','World') 
        self.assertTrue(l.remove(3).equals(LinkedList(1,2,'Hello','World')))
        l = LinkedList(1,2,3,'Hello','World') 
        self.assertTrue(l.remove('World').equals(LinkedList(1,2,3,'Hello')))

    def test_search(self):
        l = LinkedList(1,2,3,'Hello','World') 
        occurrences = l.search('Hello')
        self.assertEqual(occurrences[0].value,'Hello')

    def test_reverse(self):
        l = LinkedList(1,2,3,'Hello','World') 
        self.assertTrue(l.reverse().equals(LinkedList('World','Hello',3,2,1)))

if __name__ == '__main__':
    unittest.main()

