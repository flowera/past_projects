from linked_list import Node

class Stack(object):
    """A stack using linked list, which realizes the functions/operations of push(val) and pop()."""
    def __init__(self):
        """A Linked List Prototype."""
        self.top = Node()

    def push(self, num):
        """Stack's push operation."""
        newNode = Node(num)
        newNode.next = self.top if self.top.val else None
        self.top = newNode
    def pop(self):
        """Stack's pop operation."""
        if self.top:
            while(self.top):
                tmp = self.top
                self.top = self.top.next
                tmp.next = None
                return tmp.val
        else:
            return None
    def display(self):
        while(self.top):
            print("%d" % self.top.val, end='->')
            self.top = self.top.next
        print ('None')
