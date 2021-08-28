# Удаление дубликатов
import math


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_Node

    def print_list(self):
        p = self.head
        while p is not None:
            print(p.value)
            p = p.next

    def delete_dub(self):
        p = self.head
        while p is not None and p.next is not None:
            if p.value == p.next.value:
                q = p.next.next
                if q is None:
                    p.next = None
                    break
                p.next = q
            else:
                p = p.next


list = LinkedList()
list.append(10)
list.append(10)
list.append(10)
list.append(12)
list.append(12)
list.append(13)

list.print_list()
print("=" * 20)
list.delete_dub()
list.print_list()
