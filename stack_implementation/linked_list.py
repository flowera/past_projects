class Node():
    """Defines the Node and apply related functions."""
    def __init__(self, cargo, next=None):
        self.val = cargo
        self.next  = next
    def __str__(self):
        return str(self.val)
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self
