class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        #create dummy nodes
        self.head = Node(None,'head')
        self.tail = Node(None,'tail')
    def get_head(self):
        return self.head.next
    def get_tail(self):
        return self.tail.prev

    def add(self,node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node        