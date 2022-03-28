from typing import Any

from linked_list import LinkedList

class Queue(LinkedList):

    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return self._storage.__len__()

    def __str__(self):
        test = ''
        current = self._storage.head.next
        while current:
            test += str(current.value)
            current = current.next
            if current == None:
                break
            test += ", "
        return test

    def peek(self) -> Any:
        return self._storage.node(0).value

    def enqueue(self, element: Any):
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop().value

queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
