from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        test = ''
        current = self.head.next
        while current:
            test += str(current.value)
            current = current.next
            if current == None:
                break
            test += " -> "
        return test

    def __len__(self) -> int:
        lenght = 0
        if self.head == None:
            return lenght
        current = self.head.next
        while current:
            current = current.next
            lenght += 1
            if current == self.tail:
                break
        return lenght

    def push(self, value) -> None:
        if self.head == None:
            self.head = Node(next=None)
            self.tail = Node(next=self.head)
        newNode = Node(value=value)
        temp = self.head.next
        self.head.next = newNode
        newNode.next = temp
        if self.tail.next == self.head:
            self.tail.next = newNode
            newNode.next = None

    def append(self, value: Any) -> None:
        if self.head == None:
            self.head = Node(next=None)
            self.tail = Node(next=self.head)
        newNode = Node(value=value)
        temp = self.tail.next
        self.tail.next = newNode
        temp.next = newNode
        newNode.next = None

    def node(self, at: int) -> Node:
        if self.head == None:
            self.head = Node(next=None)
            self.tail = Node(next=self.head)
        count = 0
        current = self.head.next
        while count != at:
            if current.next == None:
                break
            count+=1
            current = current.next
        return current

    def insert(self, value: Any, after: Node) -> None:
        if self.head == None:
            self.head = Node(next=None)
            self.tail = Node(next=self.head)
        newNode = Node(value=value)
        temp = after.next
        after.next = newNode
        newNode.next = temp

    def pop(self) -> Any:
        deleted = self.head.next
        if self.tail.next == deleted:
            self.tail.next = self.head
        self.head.next = deleted.next
        return deleted

    def remove_last(self) -> Any:
        previous = None
        current = self.head.next
        while current!=self.tail.next:
            previous = current
            current = current.next
        if previous != None:
            previous.next = None
            self.tail.next = previous
        return current

    def remove(self, after: Node) -> Any:
        deleted = after.next
        after.next = deleted.next
        if deleted.next is None:
            self.tail.next = after
        return deleted


list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

# print(list_)
# print(len(list_))


